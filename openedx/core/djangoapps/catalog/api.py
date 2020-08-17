"""
Python APIs exposed by the catalog app to other in-process apps.
"""

from .utils import get_programs_by_type_slug as _get_programs_by_type_slug

def get_programs_by_type(site, program_type_slug):
    """
    Retrieves a list of programs for the site whose type's slug matches the parameter.
    Slug is used is used as a consistent value to check since ProgramType.name is
    a field that gets translated.
    """
    return _get_programs_by_type_slug(site, program_type_slug)
