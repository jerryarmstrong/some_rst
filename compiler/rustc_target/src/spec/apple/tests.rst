compiler/rustc_target/src/spec/apple/tests.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use crate::spec::{
    aarch64_apple_darwin, aarch64_apple_ios_sim, aarch64_apple_watchos_sim, i686_apple_darwin,
    x86_64_apple_darwin, x86_64_apple_ios, x86_64_apple_tvos, x86_64_apple_watchos_sim,
};

#[test]
fn simulator_targets_set_abi() {
    let all_sim_targets = [
        x86_64_apple_ios::target(),
        x86_64_apple_tvos::target(),
        x86_64_apple_watchos_sim::target(),
        aarch64_apple_ios_sim::target(),
        // Note: There is currently no ARM64 tvOS simulator target
        aarch64_apple_watchos_sim::target(),
    ];

    for target in all_sim_targets {
        assert_eq!(target.abi, "sim")
    }
}

#[test]
fn macos_link_environment_unmodified() {
    let all_macos_targets = [
        aarch64_apple_darwin::target(),
        i686_apple_darwin::target(),
        x86_64_apple_darwin::target(),
    ];

    for target in all_macos_targets {
        // macOS targets should only remove information for cross-compiling, but never
        // for the host.
        assert_eq!(target.link_env_remove, crate::spec::cvs!["IPHONEOS_DEPLOYMENT_TARGET"]);
    }
}


