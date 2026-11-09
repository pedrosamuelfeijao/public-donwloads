import unittest
from find_latest_release import newest


class SelectionTests(unittest.TestCase):
    def test_cultoflow_build_vs_version(self):
        releases=[
            {"tagName":"agent-v0.5.2-build-34","isPrerelease":True},
            {"tagName":"agent-v0.5.3-build-40","isPrerelease":True},
            {"tagName":"agent-v0.5.3-build-41","isPrerelease":True}
        ]
        self.assertEqual(newest("cultoflow","preview",releases,{"available":True,"version":"0.5.2"}),
                         ("agent-v0.5.3-build-41","0.5.3"))
        self.assertIsNone(newest("cultoflow","preview",releases,{"available":True,"version":"0.5.3"}))

    def test_rc_not_stable(self):
        releases=[
            {"tagName":"v0.4.0rc20","isPrerelease":True},
            {"tagName":"v0.4.0","isPrerelease":False}
        ]
        self.assertEqual(newest("hub","preview",releases,{"available":False}),
                         ("v0.4.0rc20","0.4.0rc20"))
        self.assertEqual(newest("compras","stable",releases,{"available":False}),
                         ("v0.4.0","0.4.0"))

    def test_bad_tags_ignored(self):
        self.assertIsNone(newest("hub","preview",[{"tagName":"invalid","isPrerelease":True}],{"available":False}))


if __name__=="__main__":unittest.main()
