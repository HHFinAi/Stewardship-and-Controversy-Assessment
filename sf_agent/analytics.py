"""Milestone and return context; not automatic engagement, voting or causal inference."""
from __future__ import annotations
import math
from .maths import COMMON_OPERATIONS, checked, number, operation, require, series
from .validation import dated,sequence,mapping,text

@operation({'milestones':'milestone_records','as_of':'ISO_date'},'milestone_progress')
def milestone_status(milestones: list[dict],as_of: str) -> dict:
    today=dated(as_of,'as_of');sequence(milestones,'milestones');seen=set();items=[]
    for m in milestones:
        mapping(m,'milestone');mid=text(m.get('id'),'milestone.id');require(mid not in seen,'duplicate milestone');seen.add(mid)
        due=dated(m.get('due_on'),'due_on');done=m.get('completed_on');verified=m.get('outcome_verified')
        require(type(verified) is bool,'outcome_verified must be boolean')
        if done is not None:require(dated(done,'completed_on')<=today,'completion is after as_of')
        require(not verified or done is not None,'verified outcome needs a completion date')
        status=('VERIFIED_OUTCOME' if verified else 'COMPLETED_UNVERIFIED') if done else ('OVERDUE' if due<today else 'PENDING')
        items.append({'id':mid,'status':status,'days_overdue':max(0,(today-due).days) if not done else 0,
                      'completion_was_late':dated(done,'completed_on')>due if done else None})
    counts={s:sum(i['status']==s for i in items) for s in ('VERIFIED_OUTCOME','COMPLETED_UNVERIFIED','OVERDUE','PENDING')}
    return {'milestones':items,'counts':counts,'verified_outcome_fraction':counts['VERIFIED_OUTCOME']/len(items) if items else None,
            'causal_engagement_success_established':False}

@operation({'security_returns':'decimal','benchmark_returns':'decimal'},'event_return_context')
def benchmark_relative_return(security_returns: list[float],benchmark_returns: list[float]) -> dict:
    sr=series(security_returns,'security_returns');br=series(benchmark_returns,'benchmark_returns')
    require(len(sr)==len(br),'return series must have equal length')
    require(all(r>=-1 for r in sr+br),'return cannot be below -100%')
    s=math.prod(1+r for r in sr)-1;b=math.prod(1+r for r in br)-1
    number(s,'security return');number(b,'benchmark return')
    return {'security_compound_return':s,'benchmark_compound_return':b,'arithmetic_excess_return':s-b,
            'relative_wealth_return':(1+s)/(1+b)-1 if b>-1 else None,'causal_event_effect_established':False}
OPERATIONS=dict(COMMON_OPERATIONS)
OPERATIONS.update({f.__name__:f for f in (milestone_status,benchmark_relative_return)})
