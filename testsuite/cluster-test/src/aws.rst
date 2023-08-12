testsuite/cluster-test/src/aws.rs
=================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use rusoto_core::Region;
use rusoto_ec2::Ec2Client;
use rusoto_ecr::EcrClient;
use rusoto_ecs::EcsClient;
use rusoto_kinesis::KinesisClient;

#[derive(Clone)]
pub struct Aws {
    workplace: String,
    kc: KinesisClient,
    ec2: Ec2Client,
    ecr: EcrClient,
    ecs: EcsClient,
}

impl Aws {
    pub fn new(workplace: String) -> Self {
        Self {
            workplace,
            kc: KinesisClient::new(Region::UsWest2),
            ec2: Ec2Client::new(Region::UsWest2),
            ecr: EcrClient::new(Region::UsWest2),
            ecs: EcsClient::new(Region::UsWest2),
        }
    }

    pub fn kc(&self) -> &KinesisClient {
        &self.kc
    }

    pub fn ec2(&self) -> &Ec2Client {
        &self.ec2
    }

    pub fn ecr(&self) -> &EcrClient {
        &self.ecr
    }

    pub fn ecs(&self) -> &EcsClient {
        &self.ecs
    }

    pub fn workplace(&self) -> &String {
        &self.workplace
    }

    pub fn region(&self) -> &str {
        Region::UsWest2.name()
    }
}


