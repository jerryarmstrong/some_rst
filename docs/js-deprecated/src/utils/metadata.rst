src/utils/metadata.ts
=====================

Last edited: 2022-06-14 09:19:26

Contents:

.. code-block:: ts

    import axios, { AxiosResponse } from 'axios';
import { MetadataJson } from './../types';

export const lookup = async (url: string): Promise<MetadataJson> => {
  try {
    const { data } = await axios.get<string, AxiosResponse<MetadataJson>>(url);

    return data;
  } catch {
    throw new Error(`unable to get metadata json from url ${url}`);
  }
};


