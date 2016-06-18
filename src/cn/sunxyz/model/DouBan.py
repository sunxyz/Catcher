'''
Created on 2016Äê4ÔÂ14ÈÕ

@author: zhuGe
'''

class DouBan(object):
    '''
    classdocs
    '''


    def __init__(self, loc_id, name, created, is_banned, is_suicide, loc_name, avatar, signature, uid, alt, desc, i_type, i_id, large_avatar):
        '''
        Constructor
        '''
        self.loc_id = loc_id
        self.name = name
        self.created = created
        self.is_banned = is_banned
        self.is_suicide = is_suicide
        self.loc_name = loc_name
        self.avatar = avatar
        self.signature = signature
        self.uid = uid
        self.alt = alt
        self.desc = desc
        self.type = i_type
        self.id = i_id
        self.large_avatar = large_avatar