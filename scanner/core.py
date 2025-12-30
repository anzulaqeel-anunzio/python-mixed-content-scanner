# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import os

class MixedContentScanner:
    # Look for src="http://..." or href="http://..." inside standard tags
    # script, img, link, iframe, audio, video, object, embed
    
    # We can be a bit more specific by looking for <tag ... src="http://..."
    # Simplified regex:
    # Match <(script|img|iframe|link|audio|video|object|embed) ... (src|href)=["']http://
    
    TAG_PATTERN = re.compile(r'<(script|img|iframe|link|audio|video|object|embed)[^>]*\s(src|href)=["\'](http://[^"\']+)["\']', re.IGNORECASE)

    @staticmethod
    def scan_file(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            # Iterate matches
            for match in MixedContentScanner.TAG_PATTERN.finditer(content):
                tag = match.group(1)
                attr = match.group(2)
                url = match.group(3)
                
                # Filter harmless
                if 'localhost' in url or '127.0.0.1' in url:
                    continue
                if 'w3.org' in url or 'schema.org' in url:
                    continue
                    
                # Find line number
                line_nm = content[:match.start()].count('\n') + 1
                
                issues.append({
                    'line': line_nm,
                    'file': filepath,
                    'tag': tag,
                    'attr': attr,
                    'url': url,
                    'msg': f'Mixed Content: Insecure {tag} resource loaded via HTTP'
                })
        except Exception:
            pass
        return issues

    @staticmethod
    def scan_directory(directory):
        all_issues = []
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                if file.endswith(('.html', '.htm', '.php', '.jsp', '.asp', '.aspx')):
                    path = os.path.join(root, file)
                    issues = MixedContentScanner.scan_file(path)
                    all_issues.extend(issues)
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
