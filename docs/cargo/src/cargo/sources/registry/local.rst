src/cargo/sources/registry/local.rs
===================================

Last edited: 2023-03-17 21:53:33

Contents:

.. code-block:: rs

    use crate::core::PackageId;
use crate::sources::registry::{LoadResponse, MaybeLock, RegistryConfig, RegistryData};
use crate::util::errors::CargoResult;
use crate::util::{Config, Filesystem};
use cargo_util::{paths, Sha256};
use std::fs::File;
use std::io::SeekFrom;
use std::io::{self, prelude::*};
use std::path::Path;
use std::task::Poll;

/// A local registry is a registry that lives on the filesystem as a set of
/// `.crate` files with an `index` directory in the same format as a remote
/// registry.
pub struct LocalRegistry<'cfg> {
    index_path: Filesystem,
    root: Filesystem,
    src_path: Filesystem,
    config: &'cfg Config,
    updated: bool,
}

impl<'cfg> LocalRegistry<'cfg> {
    pub fn new(root: &Path, config: &'cfg Config, name: &str) -> LocalRegistry<'cfg> {
        LocalRegistry {
            src_path: config.registry_source_path().join(name),
            index_path: Filesystem::new(root.join("index")),
            root: Filesystem::new(root.to_path_buf()),
            config,
            updated: false,
        }
    }
}

impl<'cfg> RegistryData for LocalRegistry<'cfg> {
    fn prepare(&self) -> CargoResult<()> {
        Ok(())
    }

    fn index_path(&self) -> &Filesystem {
        &self.index_path
    }

    fn assert_index_locked<'a>(&self, path: &'a Filesystem) -> &'a Path {
        // Note that the `*_unlocked` variant is used here since we're not
        // modifying the index and it's required to be externally synchronized.
        path.as_path_unlocked()
    }

    fn load(
        &mut self,
        root: &Path,
        path: &Path,
        _index_version: Option<&str>,
    ) -> Poll<CargoResult<LoadResponse>> {
        if self.updated {
            let raw_data = match paths::read_bytes(&root.join(path)) {
                Err(e)
                    if e.downcast_ref::<io::Error>()
                        .map_or(false, |ioe| ioe.kind() == io::ErrorKind::NotFound) =>
                {
                    return Poll::Ready(Ok(LoadResponse::NotFound));
                }
                r => r,
            }?;
            Poll::Ready(Ok(LoadResponse::Data {
                raw_data,
                index_version: None,
            }))
        } else {
            Poll::Pending
        }
    }

    fn config(&mut self) -> Poll<CargoResult<Option<RegistryConfig>>> {
        // Local registries don't have configuration for remote APIs or anything
        // like that
        Poll::Ready(Ok(None))
    }

    fn block_until_ready(&mut self) -> CargoResult<()> {
        if self.updated {
            return Ok(());
        }
        // Nothing to update, we just use what's on disk. Verify it actually
        // exists though. We don't use any locks as we're just checking whether
        // these directories exist.
        let root = self.root.clone().into_path_unlocked();
        if !root.is_dir() {
            anyhow::bail!("local registry path is not a directory: {}", root.display());
        }
        let index_path = self.index_path.clone().into_path_unlocked();
        if !index_path.is_dir() {
            anyhow::bail!(
                "local registry index path is not a directory: {}",
                index_path.display()
            );
        }
        self.updated = true;
        Ok(())
    }

    fn invalidate_cache(&mut self) {
        // Local registry has no cache - just reads from disk.
    }

    fn is_updated(&self) -> bool {
        self.updated
    }

    fn download(&mut self, pkg: PackageId, checksum: &str) -> CargoResult<MaybeLock> {
        let crate_file = format!("{}-{}.crate", pkg.name(), pkg.version());

        // Note that the usage of `into_path_unlocked` here is because the local
        // crate files here never change in that we're not the one writing them,
        // so it's not our responsibility to synchronize access to them.
        let path = self.root.join(&crate_file).into_path_unlocked();
        let mut crate_file = paths::open(&path)?;

        // If we've already got an unpacked version of this crate, then skip the
        // checksum below as it is in theory already verified.
        let dst = format!("{}-{}", pkg.name(), pkg.version());
        if self.src_path.join(dst).into_path_unlocked().exists() {
            return Ok(MaybeLock::Ready(crate_file));
        }

        self.config.shell().status("Unpacking", pkg)?;

        // We don't actually need to download anything per-se, we just need to
        // verify the checksum matches the .crate file itself.
        let actual = Sha256::new().update_file(&crate_file)?.finish_hex();
        if actual != checksum {
            anyhow::bail!("failed to verify the checksum of `{}`", pkg)
        }

        crate_file.seek(SeekFrom::Start(0))?;

        Ok(MaybeLock::Ready(crate_file))
    }

    fn finish_download(
        &mut self,
        _pkg: PackageId,
        _checksum: &str,
        _data: &[u8],
    ) -> CargoResult<File> {
        panic!("this source doesn't download")
    }
}


