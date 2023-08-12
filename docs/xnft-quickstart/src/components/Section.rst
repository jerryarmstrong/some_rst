src/components/Section.tsx
==========================

Last edited: 2023-07-18 02:03:22

Contents:

.. code-block:: tsx

    import { StyleSheet, Text, View } from "react-native";

type Props = {
  title: string;
  children: JSX.Element | JSX.Element[] | null;
};

export function Section({ title, children }: Props) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>{title}</Text>
      <View style={styles.example}>{children}</View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginBottom: 16,
  },
  title: {
    textAlign: "center",
  },
  example: {
    marginTop: 8,
  },
});


