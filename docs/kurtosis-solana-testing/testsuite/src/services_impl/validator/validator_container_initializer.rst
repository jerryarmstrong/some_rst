testsuite/src/services_impl/validator/validator_container_initializer.rs
========================================================================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    use anyhow::{Context, Result, anyhow};
use std::{borrow::BorrowMut, collections::{HashMap, HashSet}, fs::File, io::Write, path::PathBuf, rc::Rc};

use kurtosis_rust_lib::services::{docker_container_initializer::DockerContainerInitializer, service_context::ServiceContext};

use crate::services_impl::faucet::faucet_service::FaucetService;

use super::validator_service::{INIT_COMPLETE_FILEPATH, GOSSIP_PORT, RPC_PORT, ValidatorService};

const VALIDATOR_BIN_FILEPATH: &str = "/usr/bin/solana-validator";

const PORT_RANGE_FOR_GOSSIP_START: u32 = 8000;
const PORT_RANGE_FOR_GOSSIP_END: u32 = 10000;

const IDENTITY_FILE_KEY: &str = "identity-keypair";
const VOTE_ACCOUNT_FILE_KEY: &str = "vote-account-keypair";

pub (super) const TEST_VOLUME_MOUNTPOINT: &str = "/test-volume";

const SKIP_CORRUPTED_RECORD_RECOVERY_MODE: &str = "skip_any_corrupted_record";

// Where to mount the ledger directory on the validator container
const LEDGER_DIR_MOUNTPOINT: &str = "/ledger";

// Every validator can potentially run the wallet sanity check, which means they need the faucet keypair
// Thus, we write the faucet keypair to every validator's filesystem in preparation
pub (super) const FAUCET_KEYPAIR_FILEPATH: &str = "/faucet-keypair.json";

enum ValidatorType {
    FirstBootstrapper,
    ExtraBootstrapper,
}

pub struct ValidatorContainerInitializer {
	docker_image: String,
    expected_bank_hash: String,
    expected_genesis_hash: String,
    expected_shred_version: u64,
    ledger_dir_artifact_key: String,
    validator_type: ValidatorType,
    identity_keypair_json: String,
    vote_account_keypair_json: String,
    faucet: Rc<FaucetService>,
    first_bootstrapper: Option<Rc<ValidatorService>>,  // Only filled in for extra bootstrappers
}

impl<'obj> ValidatorContainerInitializer {
    pub fn for_first_bootstrapper(
        docker_image: String,
        expected_bank_hash: String,
        expected_genesis_hash: String,
        expected_shred_version: u64,
        ledger_dir_artifact_key: String,
        identity_keypair_json: String,
        vote_account_keypair_json: String,
        faucet: Rc<FaucetService>,
    ) -> ValidatorContainerInitializer {
        return ValidatorContainerInitializer{
            docker_image,
            expected_bank_hash,
            expected_genesis_hash,
            expected_shred_version,
            ledger_dir_artifact_key,
            validator_type: ValidatorType::FirstBootstrapper,
            identity_keypair_json,
            vote_account_keypair_json,
            first_bootstrapper: None,
            faucet: faucet,
        }
    }

    pub fn for_extra_bootstrapper(
        docker_image: String,
        expected_bank_hash: String,
        expected_genesis_hash: String,
        expected_shred_version: u64,
        ledger_dir_artifact_key: String,
        identity_keypair_json: String,
        vote_account_keypair_json: String,
        faucet: Rc<FaucetService>,
        bootstrapper: Rc<ValidatorService>,
    ) -> ValidatorContainerInitializer {
        return ValidatorContainerInitializer{
            docker_image,
            expected_bank_hash,
            expected_genesis_hash,
            expected_shred_version,
            ledger_dir_artifact_key,
            validator_type: ValidatorType::ExtraBootstrapper,
            identity_keypair_json,
            vote_account_keypair_json,
            first_bootstrapper: Some(bootstrapper),
            faucet: faucet,
        }
    }
}

impl DockerContainerInitializer<ValidatorService> for ValidatorContainerInitializer {
    fn get_docker_image(&self) -> &str {
        return &self.docker_image;
    }

    fn get_used_ports(&self) -> std::collections::HashSet<String> {
        let mut result = HashSet::new();
        result.insert(format!("{}/tcp", RPC_PORT));
        result.insert(format!("{}/udp", GOSSIP_PORT));
        for port in PORT_RANGE_FOR_GOSSIP_START..PORT_RANGE_FOR_GOSSIP_END {
            result.insert(format!("{}/udp", port));
        }
        return result;
    }

    fn get_service(&self, service_context: ServiceContext) -> Box<ValidatorService> {
        let service = ValidatorService::new(service_context);
        return Box::new(service);
    }

    fn get_files_to_generate(&self) -> std::collections::HashSet<String> {
        let mut result = HashSet::new();
        result.insert(String::from(IDENTITY_FILE_KEY));
        result.insert(String::from(VOTE_ACCOUNT_FILE_KEY));
        return result;
    }

    fn initialize_generated_files(&self, generated_files: HashMap<String, File>) -> Result<()> {
        for (file_key, mut fp) in generated_files {
            let file_contents;
            if file_key == IDENTITY_FILE_KEY {
                file_contents = self.identity_keypair_json.clone();
            } else if file_key == VOTE_ACCOUNT_FILE_KEY {
                file_contents = self.vote_account_keypair_json.clone();
            } else {
                return Err(anyhow!(
                    "Unrecognized file key '{}'",
                    file_key,
                ));
            }
            fp.write_all(file_contents.as_bytes())
                .context(format!("An error occurred writing the contents of the '{}' file", file_key))?;
        };
        return Ok(());
    }

    fn get_files_artifact_mountpoints(&self) -> HashMap<String, String> {
        let mut result: HashMap<String, String> = HashMap::new();
        result.insert(
            self.ledger_dir_artifact_key.clone(),
            LEDGER_DIR_MOUNTPOINT.to_owned(),
        );
        return result;
    }

    fn get_test_volume_mountpoint(&self) -> &'static str {
        return TEST_VOLUME_MOUNTPOINT;
    }

    fn get_start_command_overrides(
        &self,
        generated_file_filepaths: HashMap<String, PathBuf>,
        ip_addr: &str
    ) -> Result<(Option<Vec<String>>, Option<Vec<String>>)> {
        let identity_filepath = generated_file_filepaths.get(IDENTITY_FILE_KEY)
            .context(format!("Could not find file key '{}' in the generated filepaths map, even though we expected it", IDENTITY_FILE_KEY))?
            .to_str()
            .context(format!("Could not get path string representation of {}", IDENTITY_FILE_KEY))?;
        let vote_account_filepath = generated_file_filepaths.get(VOTE_ACCOUNT_FILE_KEY)
            .context(format!("Could not find file key '{}' in the generated filepaths map, even though we expected it", VOTE_ACCOUNT_FILE_KEY))?
            .to_str()
            .context(format!("Could not get path string representation of {}", VOTE_ACCOUNT_FILE_KEY))?;

        // We need to override the ENTRYPOINT because the Solana image has an ENTRYPOINT we don't want
        let entrypoint_args = vec![
            String::from("sh"),
            String::from("-c"),
        ];

        let mut cmd_fragments: Vec<String> = vec![
            // Write the faucet keypair to every validator's filesystem
            String::from("echo"),
            self.faucet.get_keypair_json(),
            String::from(">"),
            FAUCET_KEYPAIR_FILEPATH.to_owned(),
            String::from("&&"),

            String::from(VALIDATOR_BIN_FILEPATH),
            String::from("--rpc-port"),
            RPC_PORT.to_string(),
            String::from("--public-rpc-address"),
            format!("{}:{}", ip_addr, RPC_PORT),
            String::from("--bind-address"),
            ip_addr.to_owned(),
            String::from("--gossip-host"),
            ip_addr.to_owned(),
            String::from("--identity"),
            identity_filepath.to_owned(),
            String::from("--vote-account"),
            vote_account_filepath.to_owned(),
            String::from("--gossip-port"),
            GOSSIP_PORT.to_string(),
            String::from("--wal-recovery-mode"),
            SKIP_CORRUPTED_RECORD_RECOVERY_MODE.to_owned(),
            // This tells the nodes to wait until both are visible in gossip before they start producing blocks
            // With the stake evenly distributed between the two nodes, neither node will be able to successfully 
            // build any blocks because we'd normally need 66.6% of the network to vote on a block
            String::from("--wait-for-supermajority"),
            String::from("0"),
            // Whenever wait-for-supermajority is specified, expected-bank-hash is required
            String::from("--expected-bank-hash"),
            self.expected_bank_hash.clone(),
            String::from("--expected-genesis-hash"),
            self.expected_genesis_hash.clone(),
            String::from("--expected-shred-version"),
            self.expected_shred_version.to_string(),
            // The PoH speed test is disabled because when multiple validators are running on a single machine (i.e.
            // non-distributed Kurtosis) then things will be too slow. We try to get around this by the ledger being
            // genesis'd with `--hashes-per-tick sleep` which says "sleep rather than has to mark time" (only applicable
            // for test clusters though)
            String::from("--no-poh-speed-test"),
            String::from("--init-complete-file"),
            String::from(INIT_COMPLETE_FILEPATH),
            String::from("--ledger"), 
            LEDGER_DIR_MOUNTPOINT.to_owned(),
            String::from("--log"), 
            String::from("-"),
        ];
        match self.validator_type {
            ValidatorType::FirstBootstrapper => {
                let faucet_url = format!("{}:{}", self.faucet.get_ip_address(), self.faucet.get_port());
                cmd_fragments.append(vec![
                    String::from("--rpc-faucet-address"), 
                    faucet_url,
                ].borrow_mut());
            },
            ValidatorType::ExtraBootstrapper => {
                let bootstrapper = self.first_bootstrapper.as_ref()
                    .context("Extra bootstrapper requires a first bootstrapper, but no bootstrapper was found")?;
                let bootstrap_gossip_url = format!("{}:{}", bootstrapper.get_ip_address(), GOSSIP_PORT);
                cmd_fragments.append(vec![
                    String::from("--entrypoint"), 
                    bootstrap_gossip_url,
                    String::from("--no-snapshot-fetch"), // Doesn't need to fetch snapshot because it's starting from block 0
                    String::from("--no-genesis-fetch"), // Doesn't need to fetch genesis because it already has it
                ].borrow_mut());
            },
        }

        cmd_fragments.append(vec![
            String::from("2>&1"),
            String::from("|"),
            String::from("tee"),
            format!("{}/{}.log", TEST_VOLUME_MOUNTPOINT, ip_addr),
        ].borrow_mut());

        let cmd_args: Vec<String> = vec![
            cmd_fragments.join(" "),
        ];

        debug!("ENTRYPOINT args: {:?}", entrypoint_args);
        debug!("CMD args: {:?}", cmd_args);
        return Ok((Some(entrypoint_args), Some(cmd_args)));
    }
}

