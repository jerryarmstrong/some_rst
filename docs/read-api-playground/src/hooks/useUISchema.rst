src/hooks/useUISchema.tsx
=========================

Last edited: 2023-01-27 22:22:52

Contents:

.. code-block:: tsx

    import { useState } from "react";
import { IUISchema } from "../UISchema";

type SetSectionType = ({ section, key, value }: {
  section: string;
  key: string;
  value: any;
}) => any;

const useUISchema = (defaultValue: IUISchema): [IUISchema, SetSectionType] => {
  const [UISchema, setUISchema] = useState(defaultValue);
  const setUISchemaBySection: SetSectionType = ({ section, key, value }) => {
    setUISchema({
      ...UISchema,
      [section]: {
        ...UISchema.appBar,
        [key]: value,
      },
    });
  };
  return [UISchema, setUISchemaBySection];
};

export default useUISchema;


