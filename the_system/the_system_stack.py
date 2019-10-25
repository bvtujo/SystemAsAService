from aws_cdk import core
import aws_cdk.aws_dynamodb as dynamo
import aws_cdk.aws_lambda as awslambda
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_iam as iam


class TheSystemStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        stack = core.Stack.of(self)
        db = dynamo.Table(stack, id="MyDynamoTable", partition_key="Alias")
        arn = core.CfnOutput(
            db, 
            "DynamoCFNOutput", 
            value=db.table_arn,
            description="The arn of the DynamoDB table used as the user key/value store"
        )

        vpc = ec2.Vpc(stack, "ChimeBotVPC")
        cluster = ecs.Cluster(stack, "ChimeBotCluster", vpc=vpc)

        iam.Role(
            self, 
            id="LambdaExecutionRole", 
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaBasicExecutionRole"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AWSXrayWriteOnlyAccess"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaDynamoDBExecutionRole")
                ],
            role_name="lambda-role"
        )
        