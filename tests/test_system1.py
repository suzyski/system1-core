import unittest
import os
from system1.gate import gate_action
from system1.critic import verify_output
from system1.config import validate_credentials


class TestSystem1Core(unittest.TestCase):
    def test_credential_check(self):
        has_keys, msg = validate_credentials()
        # Ensure validate_credentials returns a boolean and string message
        self.assertIsInstance(has_keys, bool)
        self.assertIsInstance(msg, str)

    def test_gate_action_behavior(self):
        has_keys, _ = validate_credentials()
        res = gate_action("rm -rf /var/data && git push origin main --force")
        if has_keys:
            self.assertIn("top_label", res)
            self.assertEqual(res["top_label"], "high_risk_destructive")
        else:
            self.assertIn("error", res)

    def test_gate_action_safe_behavior(self):
        has_keys, _ = validate_credentials()
        res = gate_action("cat README.md && ls -la")
        if has_keys:
            self.assertIn("top_label", res)
            self.assertIn(res["top_label"], ["safe_read_or_test", "standard_edit"])
        else:
            self.assertIn("error", res)

    def test_verify_output_behavior(self):
        has_keys, _ = validate_credentials()
        res = verify_output(
            "Fix typo in index.html",
            "Fixed 'teh' to 'the' in index.html, tested in browser with 0 errors.",
        )
        if has_keys:
            self.assertIn("top_label", res)
            self.assertEqual(res["top_label"], "fully_satisfied")
        else:
            self.assertIn("error", res)


if __name__ == "__main__":
    unittest.main()
