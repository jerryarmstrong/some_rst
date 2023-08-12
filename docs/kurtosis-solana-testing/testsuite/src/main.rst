testsuite/src/main.rs
=====================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    mod execution_impl;
mod networks_impl;
mod services_impl;
mod testsuite_impl;

#[macro_use] extern crate log;

use anyhow::{Context, Result};

use clap::{App, Arg};
use execution_impl::solana_testsuite_configurator::SolanaTestsuiteConfigurator;
use kurtosis_rust_lib::execution::test_suite_executor::TestSuiteExecutor;

const CUSTOM_PARAMS_JSON_FLAG: &str = "custom-params-json";
const KURTOSIS_API_SOCKET_FLAG: &str  = "kurtosis-api-socket";
const LOG_LEVEL_FLAG: &str = "log-level";

fn main() -> Result<()> {
    let matches = App::new("My Super Program")
        .arg(Arg::new(CUSTOM_PARAMS_JSON_FLAG)
            .long(CUSTOM_PARAMS_JSON_FLAG)
            .about("JSON string containing custom data that the testsuite will deserialize to modify runtime behaviour")
            .takes_value(true)
            .value_name("JSON")
            .default_value("{}"))
        .arg(Arg::new(KURTOSIS_API_SOCKET_FLAG)
            .long(KURTOSIS_API_SOCKET_FLAG)
            .about("Socket in the form of address:port of the Kurtosis API container")
            .required(true)
            .takes_value(true)
            .value_name("IP:PORT"))
        .arg(Arg::new(LOG_LEVEL_FLAG)
            .long(LOG_LEVEL_FLAG)
            .about("String indicating the loglevel that the test suite should output with")
            .required(true)
            .takes_value(true)
            .value_name("LEVEL"))
        .get_matches();

    let custom_params_json = matches.value_of(CUSTOM_PARAMS_JSON_FLAG)
        .context(format!("No '{}' arg provided", CUSTOM_PARAMS_JSON_FLAG))?;
    let kurtosis_api_socket = matches.value_of(KURTOSIS_API_SOCKET_FLAG)
        .context(format!("No '{}' arg provided", KURTOSIS_API_SOCKET_FLAG))?;
    let log_level = matches.value_of(LOG_LEVEL_FLAG)
        .context(format!("No '{}' flag provided", LOG_LEVEL_FLAG))?;

    // >>>>>>>>>>>>>>>>>>> REPLACE WITH YOUR OWN CONFIGURATOR <<<<<<<<<<<<<<<<<<<<<<<<
	let configurator = SolanaTestsuiteConfigurator::new();
	// >>>>>>>>>>>>>>>>>>> REPLACE WITH YOUR OWN CONFIGURATOR <<<<<<<<<<<<<<<<<<<<<<<<
    
    let configurator_box = Box::from(configurator);
    let executor = TestSuiteExecutor::new(
        kurtosis_api_socket,
        log_level,
        custom_params_json,
        configurator_box
    );
    let testsuite_result = executor.run();
    if testsuite_result.is_err() {
        error!("An error occurred running the test suite executor:");
        testsuite_result.context("An error occurred running the test suite executor")?;
    }
    return Ok(());
}

