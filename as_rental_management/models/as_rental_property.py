import logging

from odoo import models, fields, api, _


_logger = logging.getLogger(__name__)


class RentalProperty(models.Model):
    _name = "as.rental.property"
    _description = "Rental Property"
