import os

import boto3
from moto import mock_aws

from files_api.s3.write_objects import upload_s3_object
from tests.consts import TEST_BUCKET_NAME


@mock_aws
def test__upload_s3_object(mocked_aws):

    # create content to write into the bucket
    object_key = "test.txt"
    file_content: bytes = b"Test Content"
    content_type = "text/plain"

    # write some information to it
    upload_s3_object(
        bucket_name=TEST_BUCKET_NAME,
        object_key=object_key,
        file_content=file_content,
        content_type=content_type,
    )
    s3_client = boto3.client("s3")
    # read the information from the bucket and check its content and metadata
    response = s3_client.get_object(Bucket=TEST_BUCKET_NAME, Key=object_key)

    assert response["Body"].read() == file_content
    assert response["ContentType"] == content_type
