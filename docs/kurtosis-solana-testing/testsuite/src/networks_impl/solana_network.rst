testsuite/src/networks_impl/solana_network.rs
=============================================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    use anyhow::{Context, Result, anyhow};
use std::{collections::{HashMap, HashSet}, rc::Rc, time::Duration};

use kurtosis_rust_lib::{core_api_bindings::api_container_api::{PartitionConnectionInfo}, networks::{network::Network, network_context::NetworkContext}, services::{availability_checker::AvailabilityChecker, service::ServiceId}};

use crate::services_impl::{faucet::{faucet_container_initializer::{FaucetContainerInitializer}, faucet_service::FaucetService}, validator::{validator_container_initializer::ValidatorContainerInitializer, validator_service::ValidatorService}};

use super::genesis_config::{FAUCET_KEYPAIR, BANK_HASH, GENESIS_HASH, SHRED_VERSION, GENESIS_BOOTSTRAPPER_KEYPAIRS};

const FAUCET_SERVICE_ID_STR: &str = "faucet";
const BOOTSTRAPPER_SERVICE_ID_PREFIX: &str = "bootstrapper-";

const FAUCET_PARTITION_ID_STR: &str = "faucet-partition";
const BOOTSTRAPPERS_PARTITION1_ID_STR: &str = "bootstrappers-partition1";
const BOOTSTRAPPERS_PARTITION2_ID_STR: &str = "bootstrappers-partition2";

const TIME_BETWEEN_BOOTSTRAPPER_AVAILABILITY_POLLS: Duration = Duration::from_secs(5);
const NUM_RETRIES_FOR_BOOTSTRAPPER_AVAILBILITY: u32 = 30;

pub struct SolanaNetwork {
    network_ctx: NetworkContext,
    ledger_dir_artifact_key: String,
    faucet: Option<Rc<FaucetService>>,
    bootstrappers: Vec<Rc<ValidatorService>>,
}

impl SolanaNetwork {
    pub fn new(network_ctx: NetworkContext, ledger_dir_artifact_key: String) -> SolanaNetwork {
        return SolanaNetwork {
            network_ctx,
            ledger_dir_artifact_key,
            faucet: None,
            bootstrappers: Vec::new(),
        }
    }

    pub fn get_num_bootstrappers(&self) -> usize {
        return GENESIS_BOOTSTRAPPER_KEYPAIRS.len();
    }

    pub fn start_faucet_and_bootstrappers(&mut self, faucet_docker_image: &str, bootstrapper_docker_image: &str) -> Result<()> {
        // Validation
        if self.faucet.is_some() {
            return Err(anyhow!(
                "Cannot start faucet because one already exists",
            ));
        }
        if self.bootstrappers.len() > 0 {
            return Err(anyhow!(
                "Cannot start bootstrappers because some already exist",
            ))
        }

        // Start the faucet
        let initializer = FaucetContainerInitializer::new(
            faucet_docker_image.to_owned(),
            FAUCET_KEYPAIR.keypair_json.to_owned(),
        );
        let (faucet, checker) = self.network_ctx.add_service(&FAUCET_SERVICE_ID_STR.to_owned(), &initializer)
            .context("An error occurred adding the faucet")?;
        checker.wait_for_startup(&TIME_BETWEEN_BOOTSTRAPPER_AVAILABILITY_POLLS, NUM_RETRIES_FOR_BOOTSTRAPPER_AVAILBILITY)
            .context("An error occurred waiting for the faucet to start")?;
        self.faucet = Some(faucet.clone());

        // Start bootstrappers
        info!("Starting bootstrappers...");
        let num_bootstrappers = GENESIS_BOOTSTRAPPER_KEYPAIRS.len();
        let mut bootstrapper_checkers: Vec<AvailabilityChecker> = Vec::new();
        for i in 0..num_bootstrappers {
            info!("Starting bootstrapper #{}...", i);
            let new_bootstrapper_keypairs = GENESIS_BOOTSTRAPPER_KEYPAIRS.get(i)
                .context(format!("Needed genesis bootstrapper keypair #{}, but genesis config doesn't have that keypair", i))?;
            let initializer;
            if i == 0 {
                initializer = ValidatorContainerInitializer::for_first_bootstrapper(
                    bootstrapper_docker_image.to_owned(), 
                    BANK_HASH.to_owned(),
                    GENESIS_HASH.to_owned(),
                    SHRED_VERSION,
                    self.ledger_dir_artifact_key.clone(),
                    new_bootstrapper_keypairs.identity.keypair_json.to_owned(),
                    new_bootstrapper_keypairs.vote_account.keypair_json.to_owned(),
                    faucet.clone(),
                );
            } else {
                let first_boostrapper = self.bootstrappers.get(0)
                    .context("Trying to start an extra bootstrapper, but no first bootstrapper was found")?;
                initializer = ValidatorContainerInitializer::for_extra_bootstrapper(
                    bootstrapper_docker_image.to_owned(), 
                    BANK_HASH.to_owned(),
                    GENESIS_HASH.to_owned(),
                    SHRED_VERSION,
                    self.ledger_dir_artifact_key.clone(),
                    new_bootstrapper_keypairs.identity.keypair_json.to_owned(),
                    new_bootstrapper_keypairs.vote_account.keypair_json.to_owned(),
                    faucet.clone(),
                    first_boostrapper.clone(),
                );

            }
            let service_id: ServiceId = format!("{}{}", BOOTSTRAPPER_SERVICE_ID_PREFIX, i);
            let (bootstrapper, checker) = self.network_ctx.add_service(&service_id, &initializer)
                .context(format!("An error occurred adding bootstrapper #{}", i))?;
            self.bootstrappers.push(bootstrapper);
            bootstrapper_checkers.push(checker);
            info!("Bootstrapper #{} started", i);
        }
        info!("Bootstrappers started");


        // Do availability-checking after starting all the nodes, because the nodes can't ever be up unless all of them
        // are started due to the genesis having all the nodes as bootstrappers
        info!("Waiting for bootstrappers to become available...");
        for i in 0..num_bootstrappers {
            info!("Waiting for bootstrapper #{} to become available...", i);
            checker.wait_for_startup(&TIME_BETWEEN_BOOTSTRAPPER_AVAILABILITY_POLLS, NUM_RETRIES_FOR_BOOTSTRAPPER_AVAILBILITY)
                .context(format!("An error occurred waiting for validator #{} to become available", i))?;
            info!("Bootstrapper #{} became available", i);
        }
        info!("Bootstrappers available");

        return Ok(());
    }

    pub fn get_bootstrapper(&self, i: usize) -> Result<&ValidatorService> {
        let bootstrapper = self.bootstrappers.get(i)
            .context(format!("Bootstrapper #{} doesn't exist", i))?;
        return Ok(bootstrapper);
    }

    /// Splits the network into two halves, with the connection between the halves blocked (or not)
    pub fn partition_in_half_with_connection(&mut self, is_connection_blocked: bool) -> Result<()> {
        let mut faucet_partition_services: HashSet<String> = HashSet::new();
        faucet_partition_services.insert(FAUCET_SERVICE_ID_STR.to_owned());

        let num_bootstrappers = self.get_num_bootstrappers();
        let first_id_in_second_partition = num_bootstrappers / 2;

        let mut bootstrappers_partition1_services: HashSet<String> = HashSet::new();
        for i in 0..first_id_in_second_partition {
            let service_id: ServiceId = SolanaNetwork::get_bootstrapper_service_id(i);
            bootstrappers_partition1_services.insert(service_id);
        }

        let mut bootstrappers_partition2_services: HashSet<String> = HashSet::new();
        for i in first_id_in_second_partition..num_bootstrappers {
            let service_id = SolanaNetwork::get_bootstrapper_service_id(i);
            bootstrappers_partition2_services.insert(service_id);
        }

        let mut partition_services: HashMap<String, HashSet<String>> = HashMap::new();
        partition_services.insert(FAUCET_PARTITION_ID_STR.to_owned(), faucet_partition_services);
        partition_services.insert(BOOTSTRAPPERS_PARTITION1_ID_STR.to_owned(), bootstrappers_partition1_services);
        partition_services.insert(BOOTSTRAPPERS_PARTITION2_ID_STR.to_owned(), bootstrappers_partition2_services);
        debug!("Partition services: {:?}", partition_services);

        let mut bootstrappers_partition1_conns: HashMap<String, PartitionConnectionInfo> = HashMap::new();
        bootstrappers_partition1_conns.insert(BOOTSTRAPPERS_PARTITION2_ID_STR.to_owned(), PartitionConnectionInfo{
            is_blocked: is_connection_blocked,
        });

        let mut partition_connections: HashMap<String, HashMap<String, PartitionConnectionInfo>> = HashMap::new();
        partition_connections.insert(BOOTSTRAPPERS_PARTITION1_ID_STR.to_owned(), bootstrappers_partition1_conns);
        debug!("Partition connections: {:?}", partition_connections);

        let default_connection_info = PartitionConnectionInfo{
            is_blocked: false,
        };

        self.network_ctx.repartition_network(
            partition_services, 
            partition_connections, 
            default_connection_info,
        ).context(format!("An error occurred partitioning the network in half, with blocked connection = {}", is_connection_blocked))?;

        return Ok(());
    }

    fn get_bootstrapper_service_id(i: usize) -> ServiceId {
        return format!("{}{}", BOOTSTRAPPER_SERVICE_ID_PREFIX, i);
    }
}

impl Network for SolanaNetwork {}

