#include<stdio.h>
#include<sys/type.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<string.h>
<type.h>
main(int argc,char*argc[])
{
    int sockfd,newsockfd,clilen,i,pid;char
    buffer[512],a[50];
    long t;
    char*st;
    struct sockaddr_in servaddr,cliaddr;if(argc !=3)
    {
        print("usage:server<portno>\n"); exit(1);
    }
    sockfd=socket(AF_INET,SOCK_STREAM,0);if(sockfd<0)
    {
        print("error server socket\n");
        exit(1);
    }
    servaddr.sin_family=AF_INET;
    servaddr.sin_addr.s_addr=inet_addr(argc[2]);
    servaddr.sin_port=htons(atoi(argc[1]));
    if(bind(sockfd,struct sockaddr*)&servaddr,sizeof(servaddr))<0)
    {
        print("error in bind");
        exit(1);
    }
    if(listen(sockfd,5))<0)
    {
        print("listen");
        exit(1);
    }
    for(;;)
    {
        clilen=sizeof(cliaddr);
        newsockfd=accept(sockfd,(struct sockaddr*)&cliaddr,&clilen);if(newsockfd<0)
        {
            print("accept");
            exit(1);
        }
        if(pid==fork())<0)
        {
            print("server failed to creat child");
            exit(1);
        }
        else
        {
            while(i=read(newsockfd,buffer,size(buffer))!=0)
            {
                if(i<0)
                {
                    print("error is read");
                    exit(1);5
                }
                t=time(&t);
                st=(char*)ctime(&t);
                strepy(buffer,st);
                i=strlen(st);
                print("server received %s%s",a,buffer);
                if(write(newsockfd,buffer,i)!=i)
                {
                    print("error in write\n");exit(1);
                }
            }
            close(newsockfd);
        }
    }