testsuite/src/testsuite_impl/simple_network_test.rs
===================================================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    use anyhow::{anyhow, Context, Result};
use std::{collections::HashMap, thread::sleep, time::Duration};

use kurtosis_rust_lib::{networks::network_context::NetworkContext, testsuite::{test::Test, test_configuration::TestConfiguration, test_context::TestContext}};

use crate::{networks_impl::{solana_network::SolanaNetwork}, };

use super::solana_testsuite::{LEDGER_DIR_ARTIFACT_KEY, LEDGER_DIR_ARTIFACT_URL};

// We don't always get new transactions produced every second, so we add a little pause to guarantee that we do
const TIME_BETWEEN_TRANSACTION_COUNT_CHECKS: Duration = Duration::from_secs(2);

const NUM_CHECK_ITERATIONS: u32 = 3;

pub struct SimpleNetworkTest {
    docker_image: String,
}

impl SimpleNetworkTest {
    pub fn new(docker_image: String) -> SimpleNetworkTest {
        return SimpleNetworkTest{
            docker_image,
        };
    }
}

impl Test for SimpleNetworkTest {
    type N = SolanaNetwork;

    fn get_test_configuration(&self) -> kurtosis_rust_lib::testsuite::test_configuration::TestConfiguration {
        let mut files_artifact_urls: HashMap<String, String> = HashMap::new();
        files_artifact_urls.insert(
            LEDGER_DIR_ARTIFACT_KEY.to_owned(), 
            LEDGER_DIR_ARTIFACT_URL.to_owned(),
        );
    
        return TestConfiguration{ 
            is_partitioning_enabled: false, 
            files_artifact_urls,
        };
    }

    fn setup(&mut self, network_ctx: NetworkContext) -> Result<Box<SolanaNetwork>> {
        let mut network = SolanaNetwork::new(
            network_ctx, 
            LEDGER_DIR_ARTIFACT_KEY.to_owned(), 
        );

        network.start_faucet_and_bootstrappers(&self.docker_image, &self.docker_image)
            .context("An error occurred starting the faucet and bootstrappers")?;

        return Ok(Box::new(network));
    }

    fn run(&self, network: Box<SolanaNetwork>, _: TestContext) -> Result<()> {
        let first_bootstrapper = network.get_bootstrapper(0)
            .context("An error occurred getting the first bootstrapper")?;

        let expected_num_nodes = network.get_num_bootstrappers();

        let mut last_bootstrapper_transaction_count_opt: Option<u64> = None;
        for i in 0..NUM_CHECK_ITERATIONS {
            info!("Asserting that the network has the correct number of nodes, {}...", expected_num_nodes);
            first_bootstrapper.assert_number_of_nodes(expected_num_nodes)
                .context(format!("An error occurred asserting that we have the expected number of nodes, '{}'", expected_num_nodes))?;
            info!("Successfully asserted that the network has the correct number of nodes");

            info!("RPC API: bootstrap-validator getTransactionCount ({})", i);
            let bootstrapper_transaction_count = first_bootstrapper.get_confirmed_transaction_count()
                .context("An error occurred getting the bootstrapper transaction count")?;

            match last_bootstrapper_transaction_count_opt.as_ref() {
                Some(last_transaction_count) => {
                    info!("Bootstrapper transaction count check: verifying that last txn count '{}' < bootstrapper txn count '{}'", last_transaction_count, bootstrapper_transaction_count);
                    if last_transaction_count >= &bootstrapper_transaction_count {
                        return Err(anyhow!(
                            "Last transaction count '{}' is >= bootstrapper transaction count '{}'; transaction count is not advancing!",
                            last_transaction_count,
                            bootstrapper_transaction_count,
                        ));
                    }
                },
                _ => {},
            }
            last_bootstrapper_transaction_count_opt = Some(bootstrapper_transaction_count);

            // Wallet sanity check
            info!("Running wallet sanity check...");
            first_bootstrapper.run_wallet_sanity_check()
                .context("An error occurred running the wallet sanity check")?;
            info!("Wallet sanity check passed");

            sleep(TIME_BETWEEN_TRANSACTION_COUNT_CHECKS);
        }

        return Ok(());
    }

    fn get_setup_timeout(&self) -> std::time::Duration {
        return Duration::from_secs(300);
    }

    fn get_execution_timeout(&self) -> std::time::Duration {
        return Duration::from_secs(240);
    }
}

