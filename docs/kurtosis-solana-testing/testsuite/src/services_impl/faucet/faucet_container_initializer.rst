testsuite/src/services_impl/faucet/faucet_container_initializer.rs
==================================================================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    use anyhow::{Context, Result, anyhow};
use std::{collections::{HashMap, HashSet}, fs::File, io::Write, path::PathBuf};

use kurtosis_rust_lib::services::{docker_container_initializer::DockerContainerInitializer, service::Service, service_context::ServiceContext};

use super::faucet_service::{FAUCET_PORT, FaucetService};

const KEYPAIR_FILE_KEY: &str = "keypair";
const TEST_VOLUME_MOUNTPOINT: &str = "/test-volume";

pub struct FaucetContainerInitializer {
    docker_image: String,
    keypair_json: String,
}

impl FaucetContainerInitializer {
    pub fn new(docker_image: String, keypair_json: String) -> FaucetContainerInitializer {
        return FaucetContainerInitializer{
            docker_image,
            keypair_json,
        };
    }
}

impl DockerContainerInitializer<FaucetService> for FaucetContainerInitializer {
    fn get_docker_image(&self) -> &str {
        return &self.docker_image;
    }

    fn get_used_ports(&self) -> HashSet<String> {
        let mut result: HashSet<String> = HashSet::new();
        result.insert(format!("{}/udp", FAUCET_PORT));
        result.insert(format!("{}/tcp", FAUCET_PORT));
        return result;
    }

    fn get_service(&self, service_context: ServiceContext) -> Box<FaucetService> {
        return Box::new(FaucetService::new(service_context, self.keypair_json.clone()));
    }

    fn get_files_to_generate(&self) -> HashSet<String> {
        let mut result: HashSet<String> = HashSet::new();
        result.insert(KEYPAIR_FILE_KEY.to_owned());
        return result;
    }

    fn initialize_generated_files(&self, generated_files: HashMap<String, File>) -> Result<()> {
        for (file_key, mut fp) in generated_files {
            if file_key == KEYPAIR_FILE_KEY {
                fp.write_all(self.keypair_json.as_bytes())
                    .context("An error occurred writing the faucet keypair JSON To file")?;
            } else {
                return Err(anyhow!(
                    "Unrecognized file key '{}'",
                    file_key,
                ));
            }
        };
        return Ok(());
    }

    fn get_files_artifact_mountpoints(&self) -> HashMap<String, String> {
        return HashMap::new();
    }


    fn get_test_volume_mountpoint(&self) -> &'static str {
        return TEST_VOLUME_MOUNTPOINT;
    }

    fn get_start_command_overrides(
        &self,
        generated_files: HashMap<String, PathBuf>,
        _: &str
    ) -> Result<(Option<Vec<String>>, Option<Vec<String>>)> {
        let keypair_json_filepath = generated_files.get(KEYPAIR_FILE_KEY)
            .context(format!("Couldn't find file key '{}' in the generated files map", KEYPAIR_FILE_KEY))?;
        let keypair_filepath_str = keypair_json_filepath.to_str()
            .context("Couldn't convert keypair filepath to string")?;
        let entrypoint_args = Some(
            vec![
                String::from("/usr/bin/solana-faucet"),
            ]
        );
        let cmd_args = Some(
            vec![
                format!("--keypair={}", keypair_filepath_str)
            ]
        );
        return Ok((entrypoint_args, cmd_args));
    }
}

