app/src/utils/validators.ts
===========================

Last edited: 2023-07-21 18:33:07

Contents:

.. code-block:: ts

    import type { ValidationError, SchemaOf } from "yup";
import { setIn, ValidationErrors } from "final-form";

export const clusterValidator =
  <T>(schema: SchemaOf<unknown>) =>
  async (values: T): Promise<boolean | ValidationErrors> => {
    try {
      await schema.validate(values, { abortEarly: false });
      return true;
    } catch (e) {
      return (e as ValidationError)?.inner.reduce(
        (errors, error) => setIn(errors, error.path || "", error.message),
        {}
      );
    }
  };


