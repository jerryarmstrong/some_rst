testsuite/src/execution_impl/solana_testsuite_configurator.rs
=============================================================

Last edited: 2021-03-14 22:40:05

Contents:

.. code-block:: rs

    use std::str::FromStr;

use anyhow::Context;
use kurtosis_rust_lib::execution::test_suite_configurator::TestSuiteConfigurator;
use log::LevelFilter;
use simplelog::{ConfigBuilder, TermLogger};

use crate::testsuite_impl::solana_testsuite::SolanaTestsuite;

use super::solana_testsuite_args::SolanaTestsuiteArgs;

pub struct SolanaTestsuiteConfigurator {}

impl SolanaTestsuiteConfigurator {
    pub fn new() -> SolanaTestsuiteConfigurator {
        return SolanaTestsuiteConfigurator{}
    }
}

impl TestSuiteConfigurator for SolanaTestsuiteConfigurator {
    fn set_log_level(&self, log_level_str: &str) -> anyhow::Result<()> {
        let config = ConfigBuilder::new()
            .set_time_format_str("%+") // From https://docs.rs/chrono/0.4.0/chrono/format/strftime/index.html#specifiers
            .build();
        let level_filter = LevelFilter::from_str(log_level_str)
            .context(format!("Could not parse log level str '{}' to a log level filter", log_level_str))?;
        TermLogger::init(level_filter, config, simplelog::TerminalMode::Mixed)
            .context("An error occurred initializing the logger")?;
        return Ok(());
    }

    fn parse_params_and_create_suite(&self, params_json_str: &str) -> anyhow::Result<Box<dyn kurtosis_rust_lib::testsuite::testsuite::TestSuite>> {
        let args: SolanaTestsuiteArgs = serde_json::from_str(params_json_str)
            .context("Could not deserialize params JSON string to testsuite args")?;
        let suite = SolanaTestsuite::new(args.normal_image);
        return Ok(Box::new(suite));
    }
}

