from asyncio.windows_events import NULL
from fileinput import filename
import math
from msilib.schema import Directory
from operator import indexOf, truediv
import os
import sys, getopt
from unicodedata import name
import subprocess
from bs4 import BeautifulSoup
import codecs
import requests
import csv
from tabulate import tabulate
import openpyxl
from os.path import exists
 
html_doc = """<div id="tournament-main-container" class="TournamentViewstyle__MainContainer-sc-dpjejw-1 caBPGm"><div class="header"><div class="ScreenTopMenu__Container-sc-12q8unn-0 qwtWc" style="height: 55px;"><div id="screen-top-menu-select-container" class="division-select-container"><div class="select-input-container"><div class="SelectInput__Container-sc-1g5pk7k-0 bfQjDl"><div class=" css-2b097c-container"><div class=" css-41kql1-control"><div class=" css-19m4gcx"><div class=" css-1gnffvl-singleValue">Open 4.5+</div><input id="react-select-2-input" readonly="" tabindex="0" aria-autocomplete="list" class="css-62g3xt-dummyInput" value=""></div><div class=" css-1wy0on6"><span class=" css-1hyfx7x"></span><div aria-hidden="true" class=" css-19zpc7z-indicatorContainer"><svg height="20" width="20" viewBox="0 0 20 20" aria-hidden="true" focusable="false" class="css-19bqh2r"><path d="M4.516 7.548c0.436-0.446 1.043-0.481 1.576 0l3.908 3.747 3.908-3.747c0.533-0.481 1.141-0.446 1.574 0 0.436 0.445 0.408 1.197 0 1.615-0.406 0.418-4.695 4.502-4.695 4.502-0.217 0.223-0.502 0.335-0.787 0.335s-0.57-0.112-0.789-0.335c0 0-4.287-4.084-4.695-4.502s-0.436-1.17 0-1.615z"></path></svg></div></div></div></div></div></div></div></div></div><div class="body"><div data-simplebar="init" class="ScrollContainer__StyledSimpleBar-sc-1qkkp7f-0 kYYpYM body-scroll-container"><div class="simplebar-wrapper" style="margin: 0px;"><div class="simplebar-height-auto-observer-wrapper"><div class="simplebar-height-auto-observer"></div></div><div class="simplebar-mask"><div class="simplebar-offset" style="right: 0px; bottom: 0px;"><div class="simplebar-content-wrapper" id="main-container-scrollable" tabindex="0" role="region" aria-label="scrollable content" style="height: 100%; overflow: hidden scroll;"><div class="simplebar-content" id="body-scroll" style="padding: 0px;"><div><div class="Box-sc-1xxy44l-0 Panelstyle__Panel-sc-16vudvk-0  cntMIm"><div><div class="Resultsstyle__Header-sc-ys52qf-2 qRGpi"><h2 class="title">Results - Open 4.5+</h2></div><div class="Resultsstyle__MessageBox-sc-ys52qf-5 dvwFyE"><h6 class="title">Is your tournament over?</h6><p>When your tournament is in the books, you can publish the <u style="font-weight: 600;">final standings</u> by using the results from the stage of your choice and make any custom change if you need to.</p><button type="button" class="BaseButton-sc-1f7jfq6-0 SolidButton-sc-1b0q07k-0 hlvvwe hDIsJd" fdprocessedid="4rap5">Publish final standings<i class="fas fa-trophy icon-right" aria-hidden="true"></i></button></div><div class="Resultsstyle__ResponsiveTableContainer-sc-ys52qf-0 iLLKZv"><table class="Resultsstyle__StyledTable-sc-ys52qf-1 iuGReo"><thead><tr><th class="team-column">Team</th><th class="record-column">Record</th><th class="icon-column"></th></tr></thead><tbody><tr class="selected"><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 56.8842px; transform: translate(-16.9805%, 0%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2FShMkAP37AUcQGbhzrSnu%2Fthumb_photo.jpg?alt=media&amp;token=ee74ee73-185a-4e74-bb0f-f8dda1824ddf" alt="Team"></div></div><div><div class="team-name">Balls In, Coming Down</div><div class="players">Max DiCerbo and Seth Cutler</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">bethany</div><div class="players">Sunny Gu and Drew Ryder</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Butter Maneuvers</div><div class="players">Michael Barkman and Rendall Weaver</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">C/S</div><div class="players">Andrew Sullivan and Cody Dryer</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Cookie Goblins</div><div class="players">Nick Evanko and Tim Lacagnina</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Cut me a break</div><div class="players">Micheal  Lin and Nathaniel Hargrove</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 56.8889px; transform: translate(-19.0338%, 0%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2FcoSoRi8gygTxknOgAz12%2Fthumb_photo.jpeg?alt=media&amp;token=162c598d-8283-491e-8160-4874631eadd3" alt="Team"></div></div><div><div class="team-name">Donner &amp; Blitzen</div><div class="players">James Richmond and Liam Sherron</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Dont talk to the girls at 20 Clearway 😤</div><div class="players">Lucas Pruett and Dennis Joseph</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 32px; transform: translate(0%, -0.493421%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2FsJB5k9HdHm50DwZMkq5g%2Fthumb_photo.jpeg?alt=media&amp;token=724a0829-99f7-4ef6-b83e-ec3295400cc7" alt="Team"></div></div><div><div class="team-name">free ballers</div><div class="players">Elie Pilon and Vincent Mathieu</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Galacticats</div><div class="players">Joey Battle and alex stan</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 32px; transform: translate(0%, -15.0454%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2FaNofqi5RqzrPIbL95CbN%2Fthumb_photo.jpeg?alt=media&amp;token=df081b52-ba9d-442d-8130-163309fc7918" alt="Team"></div></div><div><div class="team-name">Glizzy Gladiators</div><div class="players">Polk Denmark and Jacob Summers</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Gnarly </div><div class="players">Alex Newton and Sam Mccune</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">GWR Mocha Bostons</div><div class="players">Noah Henriksen and Nicolas Yabar</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">GWR Only in New York</div><div class="players">AJ Martin and Calvin Smith</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 32px; transform: translate(0%, -6.52174%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2FotlrVNBmchWZZ6D4IDx4%2Fthumb_photo.jpg?alt=media&amp;token=5f406fa2-cb2e-4d92-a21a-c487bb8354a7" alt="Team"></div></div><div><div class="team-name">GWR Pickle Boys</div><div class="players">Jacob Arzaga and Brian Perlson</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Hanukkuts</div><div class="players">Matthew Morelli and Tyler Keener</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Himothy</div><div class="players">Henry Pleszkoch and Thomas Hoffman</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Hold</div><div class="players">Maxwell Gunneson and Kevin McClain</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 36.8px; transform: translate(0%, -11.5388%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2FkE1ieC3VBDB6CAHlg3qf%2Fthumb_photo.png?alt=media&amp;token=2b2b2bce-d58a-40ac-a76e-665abff3ee8a" alt="Team"></div></div><div><div class="team-name">Idk I’m down for anything u come up with</div><div class="players">Michael Capobianco and Brody Ulrich</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 66.304px; transform: translate(-26.0114%, -14.4599%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2Fpc5G7yFqPiurLoBxmqgp%2Fthumb_photo.jpeg?alt=media&amp;token=11227bbb-84e0-4cd7-b02e-e9d3ff25a2d5" alt="Team"></div></div><div><div class="team-name">Jersey Boyz</div><div class="players">Corey Weiss and Matt Spolarich</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Katz/Sisk</div><div class="players">Griffin Sisk and Jared Dean Katz</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Klap/Model</div><div class="players">Grant Klapwijk and Cole Model</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 56.8889px; transform: translate(-21.875%, 0%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2FO6G0rjyAiizZvdn0WowH%2Fthumb_photo.png?alt=media&amp;token=739d0f4d-2f9b-4838-a917-6daf7987eedc" alt="Team"></div></div><div><div class="team-name">LafSpikes</div><div class="players">Michael Nelson and Ethan Gabay</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 91.648px; transform: translate(-42.0276%, -20.5907%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2FxO1EZRlwfcQQGrul9pha%2Fthumb_photo.png?alt=media&amp;token=cab02cd4-5d0b-4e26-8a70-bc7c002669f2" alt="Team"></div></div><div><div class="team-name">Profit Boost</div><div class="players">Kieran Rose and Justin Shaytar</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Resting Grinch Faces</div><div class="players">Samuel Corey and Zachary Troyer</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 65.3403px; transform: translate(-15.9167%, -29.5%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2FhJ0Sor28ziip0p6hHiRo%2Fthumb_photo.jpeg?alt=media&amp;token=60430032-9ba1-4dc6-bc7d-76b2a102b615" alt="Team"></div></div><div><div class="team-name">Santa’s helpers</div><div class="players">Jenson Miller and Justin Barr</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Shaytar’s kids</div><div class="players">David Rowlands and Josh Hutko</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Spike PSU</div><div class="players">Sidney Mathues and Jason Ziobro</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div class="PositionedImage__Wrapper-sc-1nn330u-0 eXa-dtp team-picture" style="width: 32px; height: 32px; border-radius: 16px;"><div class="PositionedImage__Container-sc-1nn330u-1 kdnSiE" style="width: 32px; transform: translate(0%, -20.75%);"><img src="https://firebasestorage.googleapis.com/v0/b/roundnet-4e9b0.appspot.com/o/team%2FWE3EJmGeixnwGGgrlHlE%2Fthumb_photo.jpeg?alt=media&amp;token=e18b5b57-7741-480e-be1b-7a102ba58a52" alt="Team"></div></div><div><div class="team-name">Spooky</div><div class="players">Joel Lapp and Henry Pilliod</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-users" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">SS🫤</div><div class="players">Reid Lampert and Kurt Lannetti</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Terps on Two✌️</div><div class="players">Caleb White and Brandon Fung</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Textbook</div><div class="players">Dan Savage and Mike Hamilton</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">The Rookuiz</div><div class="players">Juan Ruiz-Delgado and Ryan Fitzgerald</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Village idiots</div><div class="players">Dan Burkert and Joel Morrell</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">Why the Sheetz not?</div><div class="players">Josiah Truitt and Micah Basom </div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div </div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr><tr class=""><td class="team-column"><div class="Resultsstyle__StyledTeamItem-sc-ys52qf-4 hvmgDq"><div size="32" class="TeamPicture__PlaceholderPicture-sc-qd2z7o-0 eSDykQ team-picture"><i class="fas fa-user-friends" aria-hidden="true" style="font-size: 18.65px;"></i></div><div><div class="team-name">❓❓❓</div><div class="players">Ricky Santiago and Kevin Chen</div></div></div></td><td class="record-column"><span>0W - 0L</span></td><td class="icon-column"><i class="fas fa-chevron-right" aria-hidden="true"></i></td></tr></tbody></table></div></div></div></div></div></div></div></div><div class="simplebar-placeholder" style="width: auto; height: 2509px;"></div></div><div class="simplebar-track simplebar-horizontal" style="visibility: hidden;"><div class="simplebar-scrollbar" style="width: 0px; display: none; transform: translate3d(0px, 0px, 0px);"></div></div><div class="simplebar-track simplebar-vertical" style="visibility: visible;"><div class="simplebar-scrollbar" style="height: 123px; display: block; transform: translate3d(0px, 0px, 0px);"></div></div></div></div></div>"""
 
def main():
    soup = BeautifulSoup(html_doc, 'html.parser')
    teams = getTeams(soup)
    numPools = 6
    wb = getPoolWorksheet()
    teamSheet = wb.active
    
    playerPoints = getPlayerPoints()
    teamsSorted = sortTeams(teams, playerPoints)
    writeTeamsSheet(teamSheet, teams, playerPoints, teamsSorted, wb, numPools)
    createPoolSheet(teamsSorted, numPools, wb)
    #define header names
    col_names = ["Team", "Player One", "Player Two"]
 
    # print(tabulate(teams, headers=col_names))
    # printTeams(teams)
 
def getTeams(soup):
    teams = []
    teamNames = []
    playerOnes = []
    playerTwos = []
 
    for team in soup.findAll('div', attrs = {'class':'team-name'}):
        teamNames.append(team.text)
 
    for team in soup.findAll('div', attrs = {'class':'players'}):
        players = team.text
        andIndex = players.find(" and ")
        playerOne = players[0:andIndex]
        playerTwo = players[andIndex+5:]
        playerOnes.append(playerOne)
        playerTwos.append(playerTwo)
 
    for i in range(len(teamNames)):
        team = []
        team.append(teamNames[i])
        team.append(playerOnes[i])
        team.append(playerTwos[i])
        teams.append(team)
    return teams
 
def sortTeams(teams, playerPoints):
    sortedTeams = []
    teamsCopy = teams
    for i in range(len(teams)):
        team = getHighest(teamsCopy, playerPoints)
        sortedTeams.append(team)
        teamsCopy = removeHighestTeam(teamsCopy, team)
    # print(sortedTeams)
    return sortedTeams
 
def getHighest(teams, playerPoints):
    highestPoints = 0
    highestTeam = []
    for i in range(len(teams)):
        playerOnePoints = getPoints(teams[i][1], playerPoints[0], playerPoints[1])
        playerTwoPoints = getPoints(teams[i][2], playerPoints[0], playerPoints[1])
        teamPoints = playerOnePoints + playerTwoPoints
        if (teamPoints > highestPoints):
            highestPoints = teamPoints
            highestTeam = teams[i]
    if (highestPoints == 0):
        highestTeam = teams[0]
    highestTeam.append(highestPoints)
    return highestTeam
 
def removeHighestTeam(teams, highestTeam):
    newTeams = []
    for team in teams:
        if (equals(team, highestTeam)):
            continue
        else:
            newTeams.append(team)
    return newTeams
 
def equals(team1, team2):
    if (team1[0] == team2[0]):
        if (team1[1] == team2[1]):
            if (team1[2] == team2[2]):
                return True
    return False
 
def createPoolSheet(teamsSorted, numPools, wb):
    increasing = True
    stall = False
    poolNum = 1
    poolSheet = wb.create_sheet(title="Pools")
    for i in range(numPools):
        poolSheet.cell(row=1, column=i+1).value="Pool " + str(i+1)
    for i in range(len(teamsSorted)):
        row = math.floor(i/numPools)+2
        poolSheet.cell(row=row, column=poolNum).value = teamsSorted[i][1] + "/" + teamsSorted[i][2]
        poolNum, increasing, stall = nextPoolNum(numPools, poolNum, increasing, stall)
    wb.save('pool_calculations.xlsx')
 
 
def nextPoolNum(numPools, poolNum, increasing, stall):
    if (stall == True):
        increasing = not increasing
        stall = False
    else:
        if (increasing):
            poolNum+=1
            if (poolNum == numPools):
                stall = True
        else:
            poolNum-=1
            if (poolNum == 1):
                stall = True
    return poolNum, increasing, stall
 
def addPoolNumbers(numPools, teamSheet, teams):
    increasing = True
    stall = False
    poolNum = 1
    for i in range(len(teams)):
        teamSheet.cell(row=i+2, column=11).value=poolNum
        poolNum, increasing, stall = nextPoolNum(numPools, poolNum, increasing, stall) 
 
def writeTeamsSheet(teamSheet, teams, playerPoints, teamsSorted, wb, numPools):
    teamSheet.cell(row=1, column=1).value="Team Name"
    teamSheet.cell(row=1, column=2).value="Player One"
    teamSheet.cell(row=1, column=3).value="Player Two"
    teamSheet.cell(row=1, column=4).value="Player Names"
    teamSheet.cell(row=1, column=5).value="Player One Points"
    teamSheet.cell(row=1, column=6).value="Player Two Points"
    teamSheet.cell(row=1, column=7).value="Team Points"
    teamSheet.cell(row=1, column=9).value="Teams Sorted"
    teamSheet.cell(row=1, column=10).value="Points Sorted"
    for i in range(len(teams)):
        playerOnePoints = getPoints(teams[i][1], playerPoints[0], playerPoints[1])
        playerTwoPoints = getPoints(teams[i][2], playerPoints[0], playerPoints[1])
        teamSheet.cell(row=i+2, column=1).value=teams[i][0]
        teamSheet.cell(row=i+2, column=2).value=teams[i][1]
        teamSheet.cell(row=i+2, column=3).value=teams[i][2]
        teamSheet.cell(row=i+2, column=4).value=teams[i][1]+"/"+teams[i][2]
        teamSheet.cell(row=i+2, column=5).value=playerOnePoints
        teamSheet.cell(row=i+2, column=6).value=playerTwoPoints        
        teamSheet.cell(row=i+2, column=7).value=playerOnePoints+playerTwoPoints
        teamSheet.cell(row=i+2, column=9).value=teamsSorted[i][1] + "/" + teamsSorted[i][2]
        teamSheet.cell(row=i+2, column=10).value=teamsSorted[i][3]
    addPoolNumbers(numPools, teamSheet, teams)
    wb.save('pool_calculations.xlsx')
 
def getPlayerPoints():
    loc = os.path.join(os.getcwd(), 'player_points.xlsx')
    rd = openpyxl.load_workbook(loc, data_only=True)
    sheet = rd.active
    playerPoints = []
    names = []
    points = []
 
    for i in range(sheet.max_row):
        names.append(sheet.cell(row=i+1, column=1).value)
        points.append(sheet.cell(row=i+1, column=2).value)
    playerPoints.append(names)
    playerPoints.append(points)
    return playerPoints
 
def getPoolWorksheet():
    loc = os.path.join(os.getcwd(), 'pool_calculations.xlsx')
    if (exists(loc)):
        os.remove(loc)
    wb = openpyxl.Workbook()
    return wb
 
def getPoints(playerName, names, points):
    for i in range(len(names)):
        if (names[i] == playerName):
            return points[i]
    return 0
 
def printTeams(teams):
    for team in teams:
        print(team['teamName'], " ", team['playerOne'], " ", team['playerTwo'], "\n")
 
 
def find_nth(string, substring, n):
   if (n == 1):
       return string.find(substring)
   else:
       return string.find(substring, find_nth(string, substring, n - 1) + 1)
 
if __name__=="__main__":
    main()

