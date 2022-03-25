from flask.testing import FlaskClient
from pytest_mock import MockerFixture

from smartyard.logic.users_bank import UsersBank



def test_all(flask_client: FlaskClient, mocker: MockerFixture) -> None:
    print(flask_client, mocker)
    mocker.patch.object(UsersBank, "search_by_uuid", return_value=(79001234567,))
    mocker.patch.object(UsersBank, "update_video_token", return_value=None)
    response = flask_client.post(
        "/api/cctv/all",
        headers={"Authorization": "auth"},
        json={"1": "1"},
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.get_json()


def test_cam_map(flask_client: FlaskClient, mocker: MockerFixture) -> None:
    mocker.patch.object(UsersBank, "search_by_uuid", return_value=(79001234567,))
    response = flask_client.post("/api/cctv/camMap", headers={"Authorization": "auth"})
    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert response.get_json()


def test_overview(flask_client: FlaskClient, mocker: MockerFixture) -> None:
    mocker.patch.object(UsersBank, "search_by_uuid", return_value=(79001234567,))
    response = flask_client.post(
        "/api/cctv/overview",
        headers={"Authorization": "auth"},
        json={"1": "1"},
        content_type="application/json",
    )
    assert response.status_code == 200


def test_rec_download(flask_client: FlaskClient, mocker: MockerFixture) -> None:
    mocker.patch.object(UsersBank, "search_by_uuid", return_value=(79001234567,))
    response = flask_client.post(
        "/api/cctv/recDownload",
        headers={"Authorization": "auth"},
        json={"1": "1"},
        content_type="application/json",
    )
    assert response.status_code == 200


def test_rec_prepare(flask_client: FlaskClient, mocker: MockerFixture) -> None:
    mocker.patch.object(UsersBank, "search_by_uuid", return_value=(79001234567,))
    response = flask_client.post(
        "/api/cctv/recPrepare",
        headers={"Authorization": "auth"},
        json={"1": "1"},
        content_type="application/json",
    )
    assert response.status_code == 200


def test_youtube(flask_client: FlaskClient, mocker: MockerFixture) -> None:
    mocker.patch.object(UsersBank, "search_by_uuid", return_value=(79001234567,))
    response = flask_client.post(
        "/api/cctv/youtube",
        headers={"Authorization": "auth"},
        json={"1": "1"},
        content_type="application/json",
    )
    assert response.status_code == 200
