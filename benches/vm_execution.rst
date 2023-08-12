benches/vm_execution.rs
=======================

Last edited: 2023-08-10 08:46:13

Contents:

.. code-block:: rs

    // Copyright 2020 Solana Maintainers <maintainers@solana.com>
//
// Licensed under the Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0> or
// the MIT license <http://opensource.org/licenses/MIT>, at your option. This file may not be
// copied, modified, or distributed except according to those terms.

#![feature(test)]

extern crate solana_rbpf;
extern crate test;

use solana_rbpf::{
    ebpf,
    elf::{Executable, FunctionRegistry},
    memory_region::MemoryRegion,
    verifier::{RequisiteVerifier, TautologyVerifier},
    vm::{BuiltinProgram, Config, TestContextObject},
};
use std::{fs::File, io::Read, sync::Arc};
use test::Bencher;
use test_utils::create_vm;

#[bench]
fn bench_init_interpreter_start(bencher: &mut Bencher) {
    let mut file = File::open("tests/elfs/rodata_section.so").unwrap();
    let mut elf = Vec::new();
    file.read_to_end(&mut elf).unwrap();
    let executable = Executable::<TautologyVerifier, TestContextObject>::from_elf(
        &elf,
        Arc::new(BuiltinProgram::new_mock()),
    )
    .unwrap();
    let verified_executable =
        Executable::<RequisiteVerifier, TestContextObject>::verified(executable).unwrap();
    let mut context_object = TestContextObject::default();
    create_vm!(
        vm,
        &verified_executable,
        &mut context_object,
        stack,
        heap,
        Vec::new(),
        None
    );
    bencher.iter(|| {
        vm.context_object_pointer.remaining = 37;
        vm.execute_program(&verified_executable, true).1.unwrap()
    });
}

#[cfg(not(windows))]
#[bench]
fn bench_init_jit_start(bencher: &mut Bencher) {
    let mut file = File::open("tests/elfs/rodata_section.so").unwrap();
    let mut elf = Vec::new();
    file.read_to_end(&mut elf).unwrap();
    let executable = Executable::<TautologyVerifier, TestContextObject>::from_elf(
        &elf,
        Arc::new(BuiltinProgram::new_mock()),
    )
    .unwrap();
    let mut verified_executable =
        Executable::<RequisiteVerifier, TestContextObject>::verified(executable).unwrap();
    verified_executable.jit_compile().unwrap();
    let mut context_object = TestContextObject::default();
    create_vm!(
        vm,
        &verified_executable,
        &mut context_object,
        stack,
        heap,
        Vec::new(),
        None
    );
    bencher.iter(|| {
        vm.context_object_pointer.remaining = 37;
        vm.execute_program(&verified_executable, false).1.unwrap()
    });
}

#[cfg(not(windows))]
fn bench_jit_vs_interpreter(
    bencher: &mut Bencher,
    assembly: &str,
    config: Config,
    instruction_meter: u64,
    mem: &mut [u8],
) {
    let executable = solana_rbpf::assembler::assemble::<TestContextObject>(
        assembly,
        Arc::new(BuiltinProgram::new_loader(
            config,
            FunctionRegistry::default(),
        )),
    )
    .unwrap();
    let mut verified_executable =
        Executable::<RequisiteVerifier, TestContextObject>::verified(executable).unwrap();
    verified_executable.jit_compile().unwrap();
    let mut context_object = TestContextObject::default();
    let mem_region = MemoryRegion::new_writable(mem, ebpf::MM_INPUT_START);
    create_vm!(
        vm,
        &verified_executable,
        &mut context_object,
        stack,
        heap,
        vec![mem_region],
        None
    );
    let interpreter_summary = bencher
        .bench(|bencher| {
            bencher.iter(|| {
                vm.context_object_pointer.remaining = instruction_meter;
                let (instruction_count_interpreter, result) =
                    vm.execute_program(&verified_executable, true);
                assert!(result.is_ok(), "{:?}", result);
                assert_eq!(instruction_count_interpreter, instruction_meter);
            });
            Ok(())
        })
        .unwrap()
        .unwrap();
    let jit_summary = bencher
        .bench(|bencher| {
            bencher.iter(|| {
                vm.context_object_pointer.remaining = instruction_meter;
                let (instruction_count_jit, result) =
                    vm.execute_program(&verified_executable, false);
                assert!(result.is_ok(), "{:?}", result);
                assert_eq!(instruction_count_jit, instruction_meter);
            });
            Ok(())
        })
        .unwrap()
        .unwrap();
    println!(
        "jit_vs_interpreter_ratio={}",
        interpreter_summary.mean / jit_summary.mean
    );
}

#[cfg(not(windows))]
#[bench]
fn bench_jit_vs_interpreter_address_translation(bencher: &mut Bencher) {
    bench_jit_vs_interpreter(
        bencher,
        "
    ldxb r0, [r1]
    add r1, 1
    mov r0, r1
    and r0, 0xFFFFFF
    jlt r0, 0x20000, -5
    exit",
        Config::default(),
        655361,
        &mut [0; 0x20000],
    );
}

static ADDRESS_TRANSLATION_STACK_CODE: &str = "
    mov r1, r2
    and r1, 4095
    mov r3, r10
    sub r3, r1
    add r3, -1
    ldxb r4, [r3]
    add r2, 1
    jlt r2, 0x10000, -8
    exit";

#[cfg(not(windows))]
#[bench]
fn bench_jit_vs_interpreter_address_translation_stack_fixed(bencher: &mut Bencher) {
    bench_jit_vs_interpreter(
        bencher,
        ADDRESS_TRANSLATION_STACK_CODE,
        Config {
            enable_sbpf_v2: false,
            ..Config::default()
        },
        524289,
        &mut [],
    );
}

#[cfg(not(windows))]
#[bench]
fn bench_jit_vs_interpreter_address_translation_stack_dynamic(bencher: &mut Bencher) {
    bench_jit_vs_interpreter(
        bencher,
        ADDRESS_TRANSLATION_STACK_CODE,
        Config {
            enable_sbpf_v2: true,
            ..Config::default()
        },
        524289,
        &mut [],
    );
}

#[cfg(not(windows))]
#[bench]
fn bench_jit_vs_interpreter_empty_for_loop(bencher: &mut Bencher) {
    bench_jit_vs_interpreter(
        bencher,
        "
    mov r1, r2
    and r1, 1023
    add r2, 1
    jlt r2, 0x10000, -4
    exit",
        Config::default(),
        262145,
        &mut [0; 0],
    );
}

#[cfg(not(windows))]
#[bench]
fn bench_jit_vs_interpreter_call_depth_fixed(bencher: &mut Bencher) {
    bench_jit_vs_interpreter(
        bencher,
        "
    mov r6, 0
    add r6, 1
    mov r1, 18
    call function_foo
    jlt r6, 1024, -4
    exit
    function_foo:
    stw [r10-4], 0x11223344
    mov r6, r1
    jgt r6, 0, +1
    exit
    mov r1, r6
    add r1, -1
    call function_foo
    exit",
        Config {
            enable_sbpf_v2: false,
            ..Config::default()
        },
        137218,
        &mut [],
    );
}

#[cfg(not(windows))]
#[bench]
fn bench_jit_vs_interpreter_call_depth_dynamic(bencher: &mut Bencher) {
    bench_jit_vs_interpreter(
        bencher,
        "
    mov r6, 0
    add r6, 1
    mov r1, 18
    call function_foo
    jlt r6, 1024, -4
    exit
    function_foo:
    add r11, -4
    stw [r10-4], 0x11223344
    mov r6, r1
    jeq r6, 0, +3
    mov r1, r6
    add r1, -1
    call function_foo
    add r11, 4
    exit",
        Config {
            enable_sbpf_v2: true,
            ..Config::default()
        },
        176130,
        &mut [],
    );
}


