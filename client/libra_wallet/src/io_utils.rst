client/libra_wallet/src/io_utils.rs
===================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    // Copyright (c) The Libra Core Contributors
// SPDX-License-Identifier: Apache-2.0

//! A module to generate, store and load known users accounts.
//! The concept of known users can be helpful for testing to provide reproducible results.

use crate::*;
use failure::prelude::*;
use std::{
    fs::File,
    io::{BufRead, BufReader, Write},
    path::Path,
};

/// Delimiter used to ser/deserialize account data.
pub const DELIMITER: &str = ";";

/// Recover wallet from the path specified.
pub fn recover<P: AsRef<Path>>(path: &P) -> Result<WalletLibrary> {
    let input = File::open(path)?;
    let mut buffered = BufReader::new(input);

    let mut line = String::new();
    let _ = buffered.read_line(&mut line)?;
    let parts: Vec<&str> = line.split(DELIMITER).collect();
    ensure!(parts.len() == 2, format!("Invalid entry '{}'", line));

    let mnemonic = Mnemonic::from(&parts[0].to_string()[..])?;
    let mut wallet = WalletLibrary::new_from_mnemonic(mnemonic);
    wallet.generate_addresses(parts[1].trim().to_string().parse::<u64>()?)?;

    Ok(wallet)
}

/// Write wallet seed to file.
pub fn write_recovery<P: AsRef<Path>>(wallet: &WalletLibrary, path: &P) -> Result<()> {
    let mut output = File::create(path)?;
    writeln!(
        output,
        "{}{}{}",
        wallet.mnemonic().to_string(),
        DELIMITER,
        wallet.key_leaf()
    )?;

    Ok(())
}


