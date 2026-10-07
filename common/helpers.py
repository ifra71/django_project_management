def get_object_or_none(model, object_id):
    try:
        return model.objects.get(id=object_id)
    except model.DoesNotExist:
        return None
