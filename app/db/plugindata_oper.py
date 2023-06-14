import json
from typing import Any

from app.db import DbOper
from app.db.models import Base
from app.db.models.plugin import PluginData
from app.utils.object import ObjectUtils


class PluginDataOper(DbOper):
    """
    插件数据管理
    """

    def save(self, plugin_id: str, key: str, value: Any) -> Base:
        """
        保存插件数据
        :param plugin_id: 插件id
        :param key: 数据key
        :param value: 数据值
        """
        if ObjectUtils.is_obj(value):
            value = json.dumps(value)
        plugin = PluginData(plugin_id=plugin_id, key=key, value=value)
        return plugin.create(self._db)

    def get_data(self, key: str) -> Any:
        """
        获取插件数据
        :param key: 数据key
        """
        data = PluginData.get_plugin_data_by_key(self._db, self.__class__.__name__, key)
        if ObjectUtils.is_obj(data):
            return json.load(data)
        return data
