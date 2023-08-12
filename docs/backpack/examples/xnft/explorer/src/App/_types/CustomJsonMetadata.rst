examples/xnft/explorer/src/App/_types/CustomJsonMetadata.ts
===========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: ts

    type BundleType = "iframe" | "native";

interface CustomJsonMetadata {
  name: string;
  symbol: string;
  description: string;
  image: string;
  animation_url: string;
  external_url: string;
  properties: MetadataProperties;
}

interface MetadataProperties {
  bundle: string;
  bundle_type: BundleType;
  files: PropertiesFile[];
  versions: BundleVersion[];
}

interface BundleVersion {
  created_at: string | Date;
  uri: string;
}

interface PropertiesFile {
  uri: string;
  type: string;
}

export default CustomJsonMetadata;


