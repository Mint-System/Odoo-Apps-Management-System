import logging

from odoo import fields, models

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
        related="documentation_ids.paragraph_ids",
        string="Linked Paragraphs",
        readonly=True,
    )
