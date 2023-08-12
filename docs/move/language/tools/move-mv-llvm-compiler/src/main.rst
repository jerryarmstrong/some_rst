language/tools/move-mv-llvm-compiler/src/main.rs
================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: rs

    // Copyright (c) The Diem Core Contributors
// Copyright (c) The Move Contributors
// SPDX-License-Identifier: Apache-2.0

#![allow(unused)]

//#![forbid(unsafe_code)]

use anyhow::{bail, Context};
use clap::Parser;
use codespan_reporting::{diagnostic::Severity, term::termcolor::Buffer};
use llvm_sys::{core::LLVMContextCreate, prelude::LLVMModuleRef};
use move_binary_format::{
    binary_views::BinaryIndexedView,
    file_format::{CompiledModule, CompiledScript},
};
use move_bytecode_source_map::{mapping::SourceMapping, utils::source_map_from_file};
use move_command_line_common::files::{
    MOVE_COMPILED_EXTENSION, MOVE_EXTENSION, SOURCE_MAP_EXTENSION,
};
use move_compiler::{shared::PackagePaths, Flags};
use move_ir_types::location::Spanned;
use move_model::{
    model::GlobalEnv, options::ModelBuilderOptions, run_bytecode_model_builder, run_model_builder,
    run_model_builder_with_options_and_compilation_flags,
};
use move_mv_llvm_compiler::{cli::Args, disassembler::Disassembler};
use move_symbol_pool::Symbol as SymbolPool;
use std::{fs, path::Path};

use move_compiler::shared::NumericalAddress;
use move_stdlib::{move_stdlib_files, move_stdlib_named_addresses};

use std::path::PathBuf;

use move_mv_llvm_compiler::package::resolve_dependency;

fn main() -> anyhow::Result<()> {
    let args = Args::parse();

    if args.llvm_ir && args.obj {
        anyhow::bail!("can't output both LLVM IR (-S) and object file (-O)");
    }

    let compilation = args.compile.is_some();
    let deserialization = args.bytecode_file_path.is_some();
    let stdlib = args.stdlib;

    if compilation && deserialization {
        anyhow::bail!("can't do both: compile from source and deserialize from .mv");
    }

    if !compilation && !deserialization {
        anyhow::bail!("must set either compile or deserialize option");
    }

    if let Some(ref x) = args.move_package_path {
        let p = PathBuf::from(x);
        resolve_dependency(p, args.dev, args.test);
    }

    let global_env: GlobalEnv;
    if compilation {
        let mut deps = vec![];
        let mut named_address_map = std::collections::BTreeMap::<String, _>::new();

        if stdlib {
            named_address_map = move_stdlib_named_addresses();
            named_address_map.insert(
                "std".to_string(),
                NumericalAddress::parse_str("0x1").unwrap(),
            );

            let compiler_dependency = move_stdlib_files();

            deps.push(PackagePaths {
                name: None,
                paths: compiler_dependency,
                named_address_map: named_address_map.clone(),
            });
        }

        let target_path: String = args.compile.as_ref().unwrap().to_owned();

        if let Some(ref move_package_path_maybe) = args.move_package_path {
            let move_package_path: PathBuf = PathBuf::from(move_package_path_maybe);
            let res = resolve_dependency(move_package_path, args.dev, args.test);
            if let Ok(..) = res {
                let compiler_dependency: Vec<String> = res
                    .as_ref()
                    .unwrap()
                    .compiler_dependency
                    .iter()
                    .cloned()
                    .filter(|s| *s != target_path)
                    .collect();

                let account_addresses = res.unwrap().account_addresses;

                // Note: could use a simple chaining iterator like
                // named_address_map.extend(account_addresses.iter().map(|(sym, acc)|
                //     (sym.as_str().to_string(), NumericalAddress::parse_str(&acc.to_string()).unwrap())).into_iter());
                // but need to check for possible reassignment, so making this in old fashion loop:
                for (symbol, account_address) in account_addresses {
                    let name = symbol.as_str().to_string();
                    let address =
                        NumericalAddress::parse_str(&account_address.to_string()).unwrap();
                    if let Some(value) = named_address_map.get(&name) {
                        if *value != address {
                            bail!("{} already has assigned address {}, cannot reassign with new address {}. Possibly an error in Move.toml.",
                            name, address, *value);
                        }
                    } else {
                        named_address_map.insert(name, address);
                    }
                }

                deps.push(PackagePaths {
                    name: None,
                    paths: compiler_dependency,
                    named_address_map: named_address_map.clone(),
                });
            }
        }

        let sources = vec![PackagePaths {
            name: Some(SymbolPool::from(target_path.clone())), // TODO: is it better than `None`?
            paths: vec![target_path],
            named_address_map: named_address_map.clone(),
        }];
        let options = ModelBuilderOptions::default();
        let mut flags = if !args.test {
            Flags::verification()
        } else {
            Flags::testing()
        };

        global_env =
            run_model_builder_with_options_and_compilation_flags(sources, deps, options, flags)?;

        if global_env.diag_count(Severity::Warning) > 0 {
            let mut writer = Buffer::no_color();
            global_env.report_diag(&mut writer, Severity::Warning);
            println!("{}", String::from_utf8_lossy(&writer.into_inner()));
        }
        if global_env.diag_count(Severity::Error) > 0 {
            anyhow::bail!("Compilation failed");
        }
    } else {
        let move_extension = MOVE_EXTENSION;
        let mv_bytecode_extension = MOVE_COMPILED_EXTENSION;
        let source_map_extension = SOURCE_MAP_EXTENSION;

        let bytecode_file_path = (args.bytecode_file_path.as_ref()).unwrap();
        let source_path = Path::new(&bytecode_file_path);
        let extension = source_path
            .extension()
            .context("Missing file extension for bytecode file")?;
        if extension != mv_bytecode_extension {
            anyhow::bail!(
                "Bad source file extension {:?}; expected {}",
                extension,
                mv_bytecode_extension
            );
        }

        let bytecode_bytes =
            fs::read(bytecode_file_path).context("Unable to read bytecode file")?;

        let mut dep_bytecode_bytes = vec![];
        for dep in &args.bytecode_dependency_paths {
            let bytes = fs::read(dep).context("Unable to read dependency bytecode file {dep}")?;
            dep_bytecode_bytes.push(bytes);
        }

        let source_path = Path::new(&bytecode_file_path).with_extension(move_extension);
        let source = fs::read_to_string(&source_path).ok();
        let source_map = source_map_from_file(
            &Path::new(&bytecode_file_path).with_extension(source_map_extension),
        );

        let no_loc = Spanned::unsafe_no_loc(()).loc;
        let module: CompiledModule;
        let script: CompiledScript;
        let bytecode = if args.is_script {
            script = CompiledScript::deserialize(&bytecode_bytes)
                .context("Script blob can't be deserialized")?;
            BinaryIndexedView::Script(&script)
        } else {
            module = CompiledModule::deserialize(&bytecode_bytes)
                .context("Module blob can't be deserialized")?;
            BinaryIndexedView::Module(&module)
        };

        let mut source_mapping = {
            if let Ok(s) = source_map {
                SourceMapping::new(s, bytecode)
            } else {
                SourceMapping::new_from_view(bytecode, no_loc)
                    .context("Unable to build dummy source mapping")?
            }
        };

        if let Some(source_code) = source {
            source_mapping
                .with_source_code((source_path.to_str().unwrap().to_string(), source_code));
        }

        global_env = {
            let main_move_module = if args.is_script {
                let script = CompiledScript::deserialize(&bytecode_bytes)
                    .context("Script blob can't be deserialized")?;
                move_model::script_into_module(script)
            } else {
                CompiledModule::deserialize(&bytecode_bytes)
                    .context("Module blob can't be deserialized")?
            };

            let mut dep_move_modules = vec![];

            for bytes in &dep_bytecode_bytes {
                let dep_module = CompiledModule::deserialize(bytes)
                    .context("Dependency module blob can't be deserialized")?;
                dep_move_modules.push(dep_module);
            }

            let modules = dep_move_modules
                .into_iter()
                .chain(Some(main_move_module))
                .collect::<Vec<_>>();

            move_model::run_bytecode_model_builder(&modules)?
        }
    };

    match (&*args.gen_dot_cfg) {
        "write" | "view" | "" => {}
        _ => {
            eprintln!(
                "unexpected gen-dot-cfg option '{}', ignored.",
                &args.gen_dot_cfg
            );
        }
    };

    {
        use move_mv_llvm_compiler::stackless::{extensions::ModuleEnvExt, Target, *};

        let tgt_platform = TargetPlatform::Solana;
        tgt_platform.initialize_llvm();
        let lltarget = Target::from_triple(tgt_platform.triple())?;
        let llmachine = lltarget.create_target_machine(
            tgt_platform.triple(),
            tgt_platform.llvm_cpu(),
            tgt_platform.llvm_features(),
        );
        let global_cx = GlobalContext::new(&global_env, tgt_platform, &llmachine);

        for mod_id in global_env
            .get_modules()
            .into_iter()
            .collect::<Vec<_>>()
            .iter() // now the last is the first - use this in case of deserialization
            .rev()
            .map(|m| m.get_id())
        {
            let module = global_env.get_module(mod_id);
            let modname = module.llvm_module_name();
            let mut llmod = global_cx.llvm_cx.create_module(&modname);
            let mod_cx = global_cx.create_module_context(mod_id, &llmod, &args);
            mod_cx.translate();
            if !args.obj {
                let mut output_file = args.output_file_path.to_owned();
                // If '-c' option is set, then -o is the directory to output the compiled modules,
                // each module 'mod' will get file name 'mod.ll'
                if compilation {
                    let mut out_path = Path::new(&args.output_file_path)
                        .to_path_buf()
                        .join(modname);
                    out_path.set_extension(&args.output_file_extension);
                    output_file = out_path.to_str().unwrap().to_string();
                    match fs::create_dir_all(out_path.parent().expect("Should be a path")) {
                        Ok(_) => {}
                        Err(err) => eprintln!("Error creating directory: {}", err),
                    }
                }
                llvm_write_to_file(llmod.as_mut(), args.llvm_ir, &output_file)?;
                drop(llmod);
            } else {
                write_object_file(llmod, &llmachine, &args.output_file_path)?;
            }

            // Deserialization is always for one module, and if global env returns many,
            // after reversing the list the subject of interest is the first one.
            // For Compilation we process all modules.
            if deserialization {
                break;
            }
        }
        // NB: context must outlive llvm module
        // fixme this should be handled with lifetimes
        drop(global_cx);
    };

    Ok(())
}

fn llvm_write_to_file(
    module: LLVMModuleRef,
    llvm_ir: bool,
    output_file_name: &String,
) -> anyhow::Result<()> {
    use llvm_sys::{
        bit_writer::LLVMWriteBitcodeToFD,
        core::{LLVMDisposeMessage, LLVMPrintModuleToFile, LLVMPrintModuleToString},
    };
    use move_mv_llvm_compiler::support::to_c_str;
    use std::{ffi::CStr, fs::File, os::unix::io::AsRawFd, ptr};

    unsafe {
        if llvm_ir {
            if output_file_name != "-" {
                let mut err_string = ptr::null_mut();
                let filename = to_c_str(output_file_name);
                let res = LLVMPrintModuleToFile(module, filename.as_ptr(), &mut err_string);

                if res != 0 {
                    assert!(!err_string.is_null());
                    let msg = CStr::from_ptr(err_string).to_string_lossy();
                    LLVMDisposeMessage(err_string);
                    anyhow::bail!("{}", msg);
                }
            } else {
                let buf = LLVMPrintModuleToString(module);
                assert!(!buf.is_null());
                let cstr = CStr::from_ptr(buf);
                print!("{}", cstr.to_string_lossy());
                LLVMDisposeMessage(buf);
            }
        } else {
            if output_file_name == "-" {
                anyhow::bail!("Not writing bitcode to stdout");
            }
            let bc_file = File::create(output_file_name)?;
            let res = LLVMWriteBitcodeToFD(module, bc_file.as_raw_fd(), false as i32, true as i32);

            if res != 0 {
                anyhow::bail!("Failed to write bitcode to file");
            }
        }
    }

    Ok(())
}


