#Em três linhas de código

#Feedparser vai analiser o feed que receber da URL. Já notify2 será usado com o propósito de exibir as notificações
import feedparser
import notify2
import os
import time

def parseFeed():
   f = feed.parser('http://feeds.bbci.co.uk/news/rss.xml')
   
   ICON_PATH = os.getcwd() + "/icon.ico"
   
   notify2.init('Notícias')
   
   for newsitem in f['items']:
      n = notify2.Notification(newsintem['title'], 
      newsitem['summary'], 
      icon = ICON_PATH
      )    
   n.set_urgency(notify2.URGENCY_NORMAL)
   n.show()
   n.set_timeout(15000)
   time.sleep(1200)

   if __name__ == '__main__':
      parseFeed()