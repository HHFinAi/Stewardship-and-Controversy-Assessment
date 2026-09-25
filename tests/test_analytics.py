"""Original HHFinAi domain arithmetic tests; all numbers are synthetic."""
import copy, math, random, unittest
from sf_agent.analytics import *
from sf_agent.validation import DataError

class Stewardship(unittest.TestCase):
    def m(self,id='m',due='2026-09-01',done=None,verified=False):return {'id':id,'due_on':due,'completed_on':done,'outcome_verified':verified}
    def test_overdue(self):self.assertEqual(milestone_status([self.m()],'2026-09-25')['counts']['OVERDUE'],1)
    def test_due_today_pending(self):self.assertEqual(milestone_status([self.m(due='2026-09-25')],'2026-09-25')['counts']['PENDING'],1)
    def test_complete_unverified(self):self.assertEqual(milestone_status([self.m(done='2026-09-02')],'2026-09-25')['counts']['COMPLETED_UNVERIFIED'],1)
    def test_verified_fraction(self):self.assertEqual(milestone_status([self.m(done='2026-09-02',verified=True)],'2026-09-25')['verified_outcome_fraction'],1)
    def test_verified_needs_completion(self):
        with self.assertRaises(DataError):milestone_status([self.m(verified=True)],'2026-09-25')
    def test_completion_not_future(self):
        with self.assertRaises(DataError):milestone_status([self.m(done='2026-09-26')],'2026-09-25')
    def test_duplicate_milestone(self):
        with self.assertRaises(DataError):milestone_status([self.m(),self.m()],'2026-09-25')
    def test_empty_plan_not_zero_success(self):self.assertIsNone(milestone_status([],'2026-09-25')['verified_outcome_fraction'])
    def test_return_compounding(self):self.assertAlmostEqual(benchmark_relative_return([.1,-.1],[0,0])['security_compound_return'],-.01)
    def test_event_not_causal(self):self.assertIs(benchmark_relative_return([.1],[0])['causal_event_effect_established'],False)
    def test_benchmark_total_loss(self):self.assertIsNone(benchmark_relative_return([.1],[-1])['relative_wealth_return'])
    def test_unaligned_series(self):
        with self.assertRaises(DataError):benchmark_relative_return([.1,.2],[0])
    def test_below_total_loss(self):
        with self.assertRaises(DataError):benchmark_relative_return([-1.1],[0])

if __name__=='__main__':unittest.main()
