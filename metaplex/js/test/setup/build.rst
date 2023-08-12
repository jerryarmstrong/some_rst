metaplex/js/test/setup/build.ts
===============================

Last edited: 2022-10-11 23:41:10

Contents:

.. code-block:: ts

    import { execSync } from 'child_process';
import path from 'path';

async function build() {
  const programs: string[] = [
    'auction/program',
    'token-metadata/program',
    'token-vault/program',
    'metaplex/program',
  ];

  const currentDir = process.cwd();

  programs.forEach((directory) => {
    const dir = path.resolve(currentDir, `../../${directory}`);
    process.chdir(dir);
    execSync(`cargo build-bpf`);
  });

  process.chdir(currentDir);
}

build();


