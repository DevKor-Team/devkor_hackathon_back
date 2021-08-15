class ActionPermission:
    def get_permissions(self):
        return [
            permission()
            for permission in self.action_permission_classes.get(self.action, [])
        ]


class ActionSerializer:
    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)
