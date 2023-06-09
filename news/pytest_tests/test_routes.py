from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.parametrize(
    'parametrized_client, expected_status',
    (
        (pytest.lazy_fixture('admin_client'), HTTPStatus.NOT_FOUND),
        (pytest.lazy_fixture('author_client'), HTTPStatus.OK)
    ),
)
@pytest.mark.parametrize(
    'name, args',
    (
            ('news:edit', pytest.lazy_fixture('comment_id')),
            ('news:delete', pytest.lazy_fixture('comment_id')),
    )
)
def test_availability_for_comment_edit_and_delete(parametrized_client, expected_status, name, args):
    url = reverse(name, args=args)
    response = parametrized_client.get(url)
    assert response.status_code == expected_status


# def test_pages_availability(self):
#     pass
#
# def test_redirect_for_anonymous_client(self):
#     pass