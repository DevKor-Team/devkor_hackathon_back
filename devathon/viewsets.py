from rest_framework.viewsets import GenericViewSet, ModelViewSet


class ActionViewSet(GenericViewSet):
    def get_permissions(self):
        if hasattr(self, "action_permission_classes"):
            return [
                permission()
                for permission in self.action_permission_classes.get(
                    self.action, self.permission_classes
                )
            ]
        else:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if hasattr(self, "serializer_classes"):
            return self.serializer_classes.get(self.action, self.serializer_class)
        else:
            return self.serializer_class


class ActionModelViewSet(ActionViewSet, ModelViewSet):
    pass
