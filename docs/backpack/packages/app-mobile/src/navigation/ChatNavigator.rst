packages/app-mobile/src/navigation/ChatNavigator.tsx
====================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { createNativeStackNavigator } from "@react-navigation/native-stack";

import type { ChatStackNavigatorParamList } from "~navigation/types";
import { ChatDetailScreen } from "~screens/Unlocked/Chat/ChatDetailScreen";
import { ChatListScreen } from "~screens/Unlocked/Chat/ChatListScreen";
import {
  ChatRequestScreen,
  ChatRequestDetailScreen,
} from "~screens/Unlocked/Chat/ChatRequestScreen";

const Stack = createNativeStackNavigator<ChatStackNavigatorParamList>();
export function ChatNavigator(): JSX.Element {
  return (
    <Stack.Navigator>
      <Stack.Screen
        name="ChatList"
        component={ChatListScreen}
        options={{
          headerLargeTitle: true,
          title: "Messages",
          headerSearchBarOptions: { placeholder: "Search" },
        }}
      />
      <Stack.Screen
        name="ChatDetail"
        component={ChatDetailScreen}
        options={({ route }) => ({ title: route.params.roomName })}
      />
      <Stack.Screen
        name="ChatRequest"
        component={ChatRequestScreen}
        options={{
          title: "Requests",
        }}
      />
      <Stack.Screen
        name="ChatRequestDetail"
        component={ChatRequestDetailScreen}
        options={({ route }) => ({ title: route.params.roomName })}
      />
    </Stack.Navigator>
  );
}


