import boto3

client = boto3.client("sagemaker")

response = client.create_training_job(
    TrainingJobName="my-training-job",
    AlgorithmSpecification={
        "TrainingImage": "xxx.dkr.ecr.region.amazonaws.com/my-image:latest",
        "TrainingInputMode": "File"
    },
    RoleArn="arn:aws:iam::xxx:role/sagemaker-exec-role",
    InputDataConfig=[ ... ],
    OutputDataConfig={
        "S3OutputPath": "s3://your-bucket/output/"
    },
    ResourceConfig={
        "InstanceType": "ml.m5.large",
        "InstanceCount": 1,
        "VolumeSizeInGB": 10
    },
    StoppingCondition={"MaxRuntimeInSeconds": 3600}
)
