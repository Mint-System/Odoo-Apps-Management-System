import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class KnowledgeArticle(models.Model):
    _inherit = "knowledge.article"

    documentation_ids = fields.One2many(
        "mgmt.documentation",
        "knowledge_article_id",
        string="Referenced in Documentation",
    )

    paragraph_ids = fields.Many2many(
        "mgmt.paragraph",
        string="Linked Paragraphs",
        compute="_compute_paragraph_ids",
        store=True,
        readonly=True,
    )

    @api.depends("documentation_ids.paragraph_id")
    def _compute_paragraph_ids(self):
        for article in self:
            article.paragraph_ids = article.documentation_ids.mapped("paragraph_id")
