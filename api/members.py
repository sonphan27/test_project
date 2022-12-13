import requests


credentials = {
 'key': 'b3e408e6cce96a1ce575527f610b3885',
 'token': '123c88d46cb251880ab572ac46cfe6ce3d19f60d483cba94cac2edcb35a2ec21'
}
fmi_board_id = '5b4d2cebf11b93ca5c1daa29'
members_url = f"https://api.trello.com/1/boards/{fmi_board_id}/members"
member_info_url = f"https://api.trello.com/1/members"


def get_members():
  members = requests.get(members_url, params=credentials).json()
  members_info = []
  map_members = {}

  for member in members:
    member = requests.get(f"{member_info_url}/{member.get('id')}?fields=id,fullName,avatarUrl,username", params=credentials).json()
    members_info.append(member)
    map_members.update({member["id"]: member})
  print(map_members)
  return map_members


list_members = [
   {
      "id":"5a25ed851f14c8f71489529a",
      "username":"codenet_lylt",
      "fullName":"Le Thi Ly",
      "avatarUrl":"https://trello-members.s3.amazonaws.com/5a25ed851f14c8f71489529a/a28d6ffb0b5aa2928031a7b8dedf2e55"
   },
   {
      "id":"5ed4698e9995d57f79cb4c0d",
      "username":"namanhnguyen21896",
      "fullName":"Hope",
      "avatarUrl":"https://trello-members.s3.amazonaws.com/5ed4698e9995d57f79cb4c0d/10dc3bd8e036463c605cae40e479b0d9"
   },
   {
      "id":"5e9e68a988c2b838109b08b2",
      "username":"nguyentdat",
      "fullName":"Nguyen T Dat",
      "avatarUrl":"https://trello-members.s3.amazonaws.com/5e9e68a988c2b838109b08b2/c4efb7d18231e3e28919245eda91ed80"
   },
   {
      "id":"5e0d66ad59eeed2867d07343",
      "username":"phamgiakhanh",
      "fullName":"Pham Gia Khanh",
      "avatarUrl":"https://trello-members.s3.amazonaws.com/5e0d66ad59eeed2867d07343/e8b17554e75b1974d98feed1b36c98a8"
   },
   {
      "id":"5ed469c4d906785f412038f3",
      "username":"phanhaison",
      "fullName":"Phan Hai Son",
      "avatarUrl":"https://trello-members.s3.amazonaws.com/5ed469c4d906785f412038f3/1b1549c0dc03824ea81fe09489f634a8"
   },
   {
      "id":"59c868318665d917d07e75a0",
      "username":"codenet_phuong",
      "fullName":"codenet_phuong",
      "avatarUrl":"https://trello-members.s3.amazonaws.com/59c868318665d917d07e75a0/4e1b0fc38d1686f37bd998bad7c6cdb7"
   },
   {
      "id":"5c4111a53e5738786a15eb16",
      "username":"quanhh123",
      "fullName":"Ha Quan",
      "avatarUrl":"https://trello-members.s3.amazonaws.com/5c4111a53e5738786a15eb16/d5cee476c4f02827c4af69c1ed13af24"
   },
   {
      "id":"5dd23a9dfdd86e06fc4fd591",
      "username":"vuhienluong",
      "fullName":"Vu Hien Luong",
      "avatarUrl":"https://trello-members.s3.amazonaws.com/5dd23a9dfdd86e06fc4fd591/6cc4ad2924e7aaa28676db70a69a0620"
   },
   {
      "id":"5e40ca130242be4e60a14c77",
      "username":"thangnm_otani",
      "fullName":"nguyenminhthang",
      "avatarUrl":"https://trello-members.s3.amazonaws.com/5e40ca130242be4e60a14c77/dc8567a3298574255ac0a51af57aec73"
   },
]

map_members = {
  "5a25ed851f14c8f71489529a":{
     "id":"5a25ed851f14c8f71489529a",
     "username":"codenet_lylt",
     "fullName":"Le Thi Ly",
     "avatarUrl":"https://trello-members.s3.amazonaws.com/5a25ed851f14c8f71489529a/a28d6ffb0b5aa2928031a7b8dedf2e55"
  },
  "5ed4698e9995d57f79cb4c0d":{
     "id":"5ed4698e9995d57f79cb4c0d",
     "username":"namanhnguyen21896",
     "fullName":"Hope",
     "avatarUrl":"https://trello-members.s3.amazonaws.com/5ed4698e9995d57f79cb4c0d/10dc3bd8e036463c605cae40e479b0d9"
  },
  "5e9e68a988c2b838109b08b2":{
     "id":"5e9e68a988c2b838109b08b2",
     "username":"nguyentdat",
     "fullName":"Nguyen T Dat",
     "avatarUrl":"https://trello-members.s3.amazonaws.com/5e9e68a988c2b838109b08b2/c4efb7d18231e3e28919245eda91ed80"
  },
  "5e0d66ad59eeed2867d07343":{
     "id":"5e0d66ad59eeed2867d07343",
     "username":"phamgiakhanh",
     "fullName":"Pham Gia Khanh",
     "avatarUrl":"https://trello-members.s3.amazonaws.com/5e0d66ad59eeed2867d07343/e8b17554e75b1974d98feed1b36c98a8"
  },
  "5ed469c4d906785f412038f3":{
     "id":"5ed469c4d906785f412038f3",
     "username":"phanhaison",
     "fullName":"Phan Hai Son",
     "avatarUrl":"https://trello-members.s3.amazonaws.com/5ed469c4d906785f412038f3/1b1549c0dc03824ea81fe09489f634a8"
  },
  "59c868318665d917d07e75a0":{
     "id":"59c868318665d917d07e75a0",
     "username":"codenet_phuong",
     "fullName":"codenet_phuong",
     "avatarUrl":"https://trello-members.s3.amazonaws.com/59c868318665d917d07e75a0/4e1b0fc38d1686f37bd998bad7c6cdb7"
  },
  "5c4111a53e5738786a15eb16":{
     "id":"5c4111a53e5738786a15eb16",
     "username":"quanhh123",
     "fullName":"Ha Quan",
     "avatarUrl":"https://trello-members.s3.amazonaws.com/5c4111a53e5738786a15eb16/d5cee476c4f02827c4af69c1ed13af24"
  },
  "5dd23a9dfdd86e06fc4fd591":{
     "id":"5dd23a9dfdd86e06fc4fd591",
     "username":"vuhienluong",
     "fullName":"Vu Hien Luong",
     "avatarUrl":"https://trello-members.s3.amazonaws.com/5dd23a9dfdd86e06fc4fd591/6cc4ad2924e7aaa28676db70a69a0620"
  },
  "5e40ca130242be4e60a14c77":{
     "id":"5e40ca130242be4e60a14c77",
     "username":"thangnm_otani",
     "fullName":"nguyenminhthang",
     "avatarUrl":"https://trello-members.s3.amazonaws.com/5e40ca130242be4e60a14c77/dc8567a3298574255ac0a51af57aec73"
  },
}