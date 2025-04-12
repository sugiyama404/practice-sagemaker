import boto3

client = boto3.client("sagemaker")

client.create_training_job(
    TrainingJobName="my-training-job",
    AlgorithmSpecification={
        "TrainingImage": "354813040037.dkr.ecr.ap-northeast-1.amazonaws.com/sagemaker-xgboost:1.7-1",
        "TrainingInputMode": "File"
    },
    RoleArn="arn:aws:iam::<your_account_id>:role/sagemaker-execution-role",
    InputDataConfig=[
        {
            "ChannelName": "train",
            "DataSource": {
                "S3DataSource": {
                    "S3DataType": "S3Prefix",
                    "S3Uri": "s3://my-ml-data-bucket-1234543245422/train/",
                    "S3DataDistributionType": "FullyReplicated"
                }
            },
            "ContentType": "text/csv"
        }
    ],
    OutputDataConfig={
        "S3OutputPath": "s3://my-ml-data-bucket-1234543245422/output/"
    },
    ResourceConfig={
        "InstanceType": "ml.m5.large",
        "InstanceCount": 1,
        "VolumeSizeInGB": 10
    },
    StoppingCondition={
        "MaxRuntimeInSeconds": 3600
    },
    HyperParameters={
        "max_depth": "5",
        "eta": "0.2",
        "objective": "reg:squarederror",  # 回帰タスク用。分類なら変更
        "num_round": "100",
        "verbosity": "1"
    }
)
