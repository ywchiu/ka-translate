import urllib
import urllib2
import re


class getsubtitle:
	def __init__(self):
		self.url = 'http://www.universalsubtitles.org/en/videos/create/'

	def subtitleReader(self, file_name):
		f = open(file_name, 'r')
		for line in f.readlines():
			ele = line.split('\n')
			sub_ele = ele[0].split('\t')
			self.subtitleCrawler(sub_ele[2],sub_ele[1])
			print sub_ele[1],sub_ele[2]

	def subtitleCrawler(self, sub_id, sub_name):
		form_data = {'video_url':'http://www.youtube.com/watch?v=%s'%(sub_id)}
		params = urllib.urlencode(form_data)
		response = urllib2.urlopen(self.url, params)
		response_url = response.geturl()

		video_id = re.findall(r'videos/(.*?)/info',response_url)[0]
		video_response = urllib2.urlopen(response_url)
		data = video_response.read()

		matched_txt = re.findall(r'<a href.*?zh-cn/([0-9]+)/',data)[0]
		download_link = 'http://www.universalsubtitles.org/widget/download_srt/?video_id=%s&lang_pk=%s' %(video_id,matched_txt)
		urllib.urlretrieve (download_link, "subtitle/%s.srt"%(sub_name))
