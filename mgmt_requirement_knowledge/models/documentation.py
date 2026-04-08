import logging

from odoo import api, fields, models
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class MgmtDocumentation(models.Model):
    _name = "mgmt.documentation"
    _description = "Mgmt Documentation"

    type = fields.Selection(
        [
            ("url", "Url"),
            ("wiki", "Wiki Page"),
        ],
        required=True,
    )

    url = fields.Char(string="URL")
    name = fields.Char(string="Name")

    knowledge_article_id = fields.Many2one(
        "knowledge.article",
        string="Knowledge Article",
        ondelete="restrict",
    )
    paragraph_id = fields.Many2one("mgmt.paragraph")

    @api.constrains("type", "url", "name", "knowledge_article_id")
    def _check_documentation_type(self):
        for rec in self:
            if rec.type == "url":
                if not rec.url:
                    raise ValidationError("URL must be set when documentation type is 'Web link'.")
                if not rec.name:
                    raise ValidationError("Name must be set when documentation type is 'Web link'.")
                if rec.knowledge_article_id:
                    raise ValidationError("Knowledge article must be empty when type is 'Web link'.")

            if rec.type == "wiki":
                if not rec.knowledge_article_id:
                    raise ValidationError(
                        "Knowledge article must be set when documentation type is 'Knowledge article'."
                    )
                if rec.url:
                    raise ValidationError("URL must be empty when type is 'Knowledge article'.")

    @api.onchange("url", "knowledge_article_id", "type")
    def _onchange_name(self):
        if self.type == "url" and self.url:
            self.name = self.url
        elif self.type == "wiki" and self.knowledge_article_id:
            self.name = self.knowledge_article_id.name
