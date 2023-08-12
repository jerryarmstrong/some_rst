packages/tamagui-core/src/components/SearchBox.tsx
==================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { Input } from "tamagui";

export const SearchBox = ({
  onChange,
  placeholder,
  searchFilter,
  setSearchFilter,
}: {
  onChange: any;
  placeholder?: string;
  searchFilter: string;
  setSearchFilter: any;
}) => {
  // const theme = useCustomTheme()
  return (
    <Input
      size="$input"
      placeholder={placeholder ?? "Enter a username or address"}
      value={searchFilter}
      onChangeText={(text: string) => {
        setSearchFilter(text);
        onChange(text);
      }}
    />
  );
};


