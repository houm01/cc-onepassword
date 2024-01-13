#!/usr/bin/env python3

import os
from onepasswordconnectsdk.client import (
    Client,
    new_client_from_environment,
    new_client
)

class OnePassword:

    def __init__(self, default_valut_id: str=None):
        '''
        需要设置环境变量 OP_CONNECT_HOST 和 OP_CONNECT_TOKEN

        Args:
            default_value_id (_type_): 默认的 
        '''
        self.client = new_client_from_environment()
        if not default_valut_id:
            self.default_valut_id = os.environ.get('ONEPASSWORD_DEFAULT_VALUT_ID')
        else:
            self.default_valut_id = default_valut_id

    def get_items(self, vault_id):
        return self.client.get_items(vault_id)

    def get_item(self, item_id, vault_id):
        return self.client.get_item(item_id, vault_id)

    def insert_item(self, vault_id, item):
        return self.client.create_item(vault_id, item)

    def delete_item(self, vault_id, item_id):
        return self.client.delete_item(vault_id, item_id)

    def get_password(self, item):
        for field in item["fields"]:
            if field["designation"] == "password":
                return field["value"]
    
    def get_item_by_title(self, title: str='', totp: bool=False):
        '''通过title获取具体的值, 会返回一个字典'''
        value = {}
        item = self.client.get_item_by_title(title, self.default_valut_id)

        if totp:
            for field in item.fields:
                if field.totp != None:
                    return field.totp
        else:
            for field in item.fields:
                value[field.label] = field.value
            return value

    def update_item(self, title: str, name: str, value: str):
        '''
        更新单个item
        Parms:
            title(str): 一条数据的名称
            name(str): 需要更新的参数值, 例如 username, password
            value(str): 新的值
        Returns:
            Item object(class): 更新后的item
        '''

        item = self.client.get_item_by_title(title, self._valut_id_my1p)

        num = 0

        for field in item.fields:

            if field.label == name:
                item.fields[num].value = value
            num += 1

        try:
            result = self.client.update_item(vault_id=self._valut_id_my1p, item=item, item_uuid=item.id)
            return result
        except Exception as e:
            return e


if __name__ == "__main__":
    pass
    