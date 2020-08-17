from typing import List
from opaque_keys.edx.keys import CourseKey

from course_modes.models import _CourseMode


def get_paid_modes_for_course(course_run_id: CourseKey) -> List[str]:
    """
    Returns a list of non-expired mode slugs for a course run ID that have a set minimum price.
    """
    return _CourseMode.paid_modes_for_course(course_run_id)
