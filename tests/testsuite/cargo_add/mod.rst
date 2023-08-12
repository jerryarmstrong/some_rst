tests/testsuite/cargo_add/mod.rs
================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    mod add_basic;
mod add_multiple;
mod add_normalized_name_external;
mod build;
mod build_prefer_existing_version;
mod change_rename_target;
mod default_features;
mod deprecated_default_features;
mod deprecated_section;
mod detect_workspace_inherit;
mod detect_workspace_inherit_features;
mod detect_workspace_inherit_optional;
mod dev;
mod dev_build_conflict;
mod dev_prefer_existing_version;
mod dry_run;
mod features;
mod features_empty;
mod features_multiple_occurrences;
mod features_preserve;
mod features_spaced_values;
mod features_unknown;
mod features_unknown_no_features;
mod git;
mod git_branch;
mod git_conflicts_namever;
mod git_dev;
mod git_inferred_name;
mod git_inferred_name_multiple;
mod git_multiple_names;
mod git_normalized_name;
mod git_registry;
mod git_rev;
mod git_tag;
mod infer_prerelease;
mod invalid_arg;
mod invalid_git_external;
mod invalid_git_name;
mod invalid_key_inherit_dependency;
mod invalid_key_overwrite_inherit_dependency;
mod invalid_key_rename_inherit_dependency;
mod invalid_manifest;
mod invalid_name_external;
mod invalid_path;
mod invalid_path_name;
mod invalid_path_self;
mod invalid_target_empty;
mod invalid_vers;
mod list_features;
mod list_features_path;
mod list_features_path_no_default;
mod locked_changed;
mod locked_unchanged;
mod lockfile_updated;
mod manifest_path_package;
mod merge_activated_features;
mod multiple_conflicts_with_features;
mod multiple_conflicts_with_rename;
mod namever;
mod no_args;
mod no_default_features;
mod no_optional;
mod offline_empty_cache;
mod optional;
mod overwrite_default_features;
mod overwrite_default_features_with_no_default_features;
mod overwrite_features;
mod overwrite_git_with_path;
mod overwrite_inherit_features_noop;
mod overwrite_inherit_noop;
mod overwrite_inherit_optional_noop;
mod overwrite_inline_features;
mod overwrite_name_dev_noop;
mod overwrite_name_noop;
mod overwrite_no_default_features;
mod overwrite_no_default_features_with_default_features;
mod overwrite_no_optional;
mod overwrite_no_optional_with_optional;
mod overwrite_optional;
mod overwrite_optional_with_no_optional;
mod overwrite_path_noop;
mod overwrite_path_with_version;
mod overwrite_preserves_inline_table;
mod overwrite_rename_with_no_rename;
mod overwrite_rename_with_rename;
mod overwrite_rename_with_rename_noop;
mod overwrite_version_with_git;
mod overwrite_version_with_path;
mod overwrite_with_rename;
mod overwrite_workspace_dep;
mod overwrite_workspace_dep_features;
mod path;
mod path_dev;
mod path_inferred_name;
mod path_inferred_name_conflicts_full_feature;
mod path_normalized_name;
mod preserve_sorted;
mod preserve_unsorted;
mod quiet;
mod registry;
mod rename;
mod require_weak;
mod target;
mod target_cfg;
mod unknown_inherited_feature;
mod vers;
mod workspace_name;
mod workspace_path;
mod workspace_path_dev;

fn init_registry() {
    cargo_test_support::registry::init();
    add_registry_packages(false);
}

fn init_alt_registry() {
    cargo_test_support::registry::alt_init();
    add_registry_packages(true);
}

fn add_registry_packages(alt: bool) {
    for name in [
        "my-package",
        "my-package1",
        "my-package2",
        "my-dev-package1",
        "my-dev-package2",
        "my-build-package1",
        "my-build-package2",
        "toml",
        "versioned-package",
        "cargo-list-test-fixture-dependency",
        "unrelateed-crate",
    ] {
        cargo_test_support::registry::Package::new(name, "0.1.1+my-package")
            .alternative(alt)
            .publish();
        cargo_test_support::registry::Package::new(name, "0.2.0+my-package")
            .alternative(alt)
            .publish();
        cargo_test_support::registry::Package::new(name, "0.2.3+my-package")
            .alternative(alt)
            .publish();
        cargo_test_support::registry::Package::new(name, "0.4.1+my-package")
            .alternative(alt)
            .publish();
        cargo_test_support::registry::Package::new(name, "20.0.0+my-package")
            .alternative(alt)
            .publish();
        cargo_test_support::registry::Package::new(name, "99999.0.0+my-package")
            .alternative(alt)
            .publish();
        cargo_test_support::registry::Package::new(name, "99999.0.0-alpha.1+my-package")
            .alternative(alt)
            .publish();
    }

    cargo_test_support::registry::Package::new("prerelease_only", "0.2.0-alpha.1")
        .alternative(alt)
        .publish();
    cargo_test_support::registry::Package::new("test_breaking", "0.2.0")
        .alternative(alt)
        .publish();
    cargo_test_support::registry::Package::new("test_nonbreaking", "0.1.1")
        .alternative(alt)
        .publish();

    // Normalization
    cargo_test_support::registry::Package::new("linked-hash-map", "0.5.4")
        .alternative(alt)
        .feature("clippy", &[])
        .feature("heapsize", &[])
        .feature("heapsize_impl", &[])
        .feature("nightly", &[])
        .feature("serde", &[])
        .feature("serde_impl", &[])
        .feature("serde_test", &[])
        .publish();
    cargo_test_support::registry::Package::new("inflector", "0.11.4")
        .alternative(alt)
        .feature("default", &["heavyweight", "lazy_static", "regex"])
        .feature("heavyweight", &[])
        .feature("lazy_static", &[])
        .feature("regex", &[])
        .feature("unstable", &[])
        .publish();

    cargo_test_support::registry::Package::new("your-face", "99999.0.0+my-package")
        .alternative(alt)
        .feature("nose", &[])
        .feature("mouth", &[])
        .feature("eyes", &[])
        .feature("ears", &[])
        .publish();
}


