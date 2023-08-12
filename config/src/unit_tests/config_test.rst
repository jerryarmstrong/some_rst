config/src/unit_tests/config_test.rs
====================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

use super::*;
use std::fs;

#[test]
fn verify_test_config() {
    // This test verifies that the default config in config.toml is valid
    let _ = NodeConfigHelpers::get_single_node_test_config(false);
}

#[test]
fn verify_all_configs() {
    // This test verifies that all configs in data/config are valid
    let paths = fs::read_dir("data/configs").expect("cannot read config dir");

    for path in paths {
        let config_path = path.unwrap().path();
        let config_path_str = config_path.to_str().unwrap();
        if config_path_str.ends_with(".toml") {
            println!("Loading {}", config_path_str);
            let _ = NodeConfig::load(config_path_str).expect("NodeConfig");
        } else {
            println!("Invalid file {} for verifying", config_path_str);
        }
    }
}


