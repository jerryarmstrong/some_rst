src/hooks/useParsedSchema.tsx
=============================

Last edited: 2023-01-27 22:22:52

Contents:

.. code-block:: tsx

    import { useState, useEffect, Dispatch } from "react";
import _ from "lodash";
import refParser from "json-schema-ref-parser";
import { OpenrpcDocument } from "@open-rpc/meta-schema";

const useParsedSchema = (defaultValue: object | any): [OpenrpcDocument | undefined, Dispatch<string>] => {
  const [parsedSchema, setParsedSchema]: [OpenrpcDocument | undefined, Dispatch<OpenrpcDocument>] = useState();
  const validateAndSetSchema = (schema: string) => {
    let maybeSchema: string | undefined;
    try {
      maybeSchema = JSON.parse(schema);
    } catch (e) {
      //
    }
    if (!maybeSchema) {
      return;
    }
    refParser.dereference(maybeSchema).then((dereferencedSchema) => {
      setParsedSchema(dereferencedSchema as OpenrpcDocument);
      // set original non-dereff'd schema to localstorage
      _.defer(() => window.localStorage.setItem("schema", schema as string));
    });
  };
  useEffect(() => {
    if (defaultValue) {
      validateAndSetSchema(defaultValue);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  return [parsedSchema, validateAndSetSchema];
};

export default useParsedSchema;


