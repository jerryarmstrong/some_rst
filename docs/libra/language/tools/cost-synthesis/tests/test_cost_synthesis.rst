language/tools/cost-synthesis/tests/test_cost_synthesis.rs
==========================================================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: rs

    use std::{env, path::PathBuf, process::Command};

// Path to cargo executables
pub fn cargo_dir() -> PathBuf {
    env::var_os("CARGO_BIN_PATH")
        .map(PathBuf::from)
        .or_else(|| {
            env::current_exe().ok().map(|mut path| {
                path.pop();
                if path.ends_with("deps") {
                    path.pop();
                }
                path
            })
        })
        .unwrap_or_else(|| panic!("CARGO_BIN_PATH wasn't set. Cannot continue running test"))
}

pub fn cost_synthesis_exe() -> PathBuf {
    cargo_dir().join(format!(
        "solana-libra-cost-synthesis{}",
        env::consts::EXE_SUFFIX
    ))
}

#[test]
fn test_cost_synthesis() {
    let output = Command::new(cost_synthesis_exe())
        .args(&["-i", "10"])
        .output()
        .unwrap()
        .stderr;
    println!("errors: {}", String::from_utf8_lossy(&output));
}


