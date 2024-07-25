from odoo.tests.common import TransactionCase


class TestAudit(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.Audit = self.env["mgmt.audit"]
        self.audit1 = self.Audit.create(
            {"name": "Test Audit", "reference": "879-1-78439-279-6"}
        )

    def test_audit_create(self):
        "Name shoult not be empty"
        self.assertNotEqual(self.audit1.name, False)
