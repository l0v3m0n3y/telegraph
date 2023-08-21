import requests
class Client():
	def __init__(self,token:str=None):
		self.api="https://api.telegra.ph"
		self.token=token
	def create_Account(self,short_name,nickname,url_account):
		url=f"{self.api}/createAccount?short_name={short_name}&author_name={nickname}"
		if url_account:url=f"{url}&author_url={url_account}"
		request=requests.get(url).json()["result"]
		self.token= request['access_token']
		return request
	def edit_Account(self,short_name:str=None,author_name:str=None,author_url:str=None):
		url=f"{self.api}/editAccountInfo?access_token={self.token}"
		if short_name: url=f"{url}&short_name={short_name}"
		if author_name: url=f"{url}&author_name={author_name}"
		if author_url:url=f"{url}&author_url={author_url}"
		return requests.get(url).json()
	def revoke_Token(self):
		request=requests.get(f"{self.api}/revokeAccessToken?access_token={self.token}").json()
		self.token=request["result"]["access_token"]
		return request
	def create_Page(self,author_name,title,author_url:str=None,content:str=None,return_content:str=None):
		url=f"{self.api}/createPage?access_token={self.token}&author_name={author_name}&title={title}"
		if author_url:url=f"{url}&author_url={author_url}"
		if return_content:url=f"{url}&return_content=true"
		if content:url=f"{url}&content={content}"
		return requests.get(url).json()
	def edit_Page(self,author_name,title,author_url:str=None,content:str=None,return_content:str=None):
		url=f"{self.api}/editPage?access_token={self.token}&author_name={author_name}&title={title}"
		if author_url:url=f"{url}&author_url={author_url}"
		if return_content:url=f"{url}&return_content=true"
		if content:url=f"{url}&content={content}"
		return requests.get(url).json()
	def get_Page(self,page_name,return_content:str=None):
		url=f"{self.api}/getPage?{page_name}"
		if return_content:url=f"{url}&return_content=true"
		return requests.get(url).json()
	def get_Page_List(self,start:int=0,size:int=100):
		return requests.get(f"{self.api}/getPageList?access_token={self.token}&offset={start}&limit={size}").json()
	def get_Views(self,page_name,year,month,day:int=None):
		url=f"{self.api}/getViews?{page_name}&year={year}&month={month}"
		if day: url=f"{url}&day={day}"
		return requests.get(url).json()
	def get_Account_Info(self):
		return requests.get(f"{self.api}/getAccountInfo?access_token={self.token}&['short_name','page_count''author_name','author_url','auth_url']").json()